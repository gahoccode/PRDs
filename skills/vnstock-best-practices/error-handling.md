# Error Handling Patterns for VNStock Quote

## Circuit Breaker

Stops requests after repeated failures, auto-recovers after timeout:

```python
from datetime import datetime, timedelta

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout_seconds=60):
        self.failure_threshold = failure_threshold
        self.timeout_seconds = timeout_seconds
        self.failure_count = 0
        self.last_failure = None
        self.is_open = False
    
    def call(self, func, *args, **kwargs):
        if self.is_open:
            if datetime.now() - self.last_failure > timedelta(seconds=self.timeout_seconds):
                self.is_open = False
                self.failure_count = 0
            else:
                raise Exception("Circuit open - service unavailable")
        
        try:
            result = func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure = datetime.now()
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
            raise e

# Usage
from vnstock import Quote

circuit = CircuitBreaker(failure_threshold=3, timeout_seconds=60)
quote = Quote(source='VCI', symbol='VCI')

df = circuit.call(quote.history, start='2024-01-01', end='2024-12-31')
```

## Connection Pool

Reuse Quote instances across threads:

```python
from vnstock import Quote
import threading
from queue import Queue

class QuotePool:
    """VNStock Quote Connection Pool"""
    
    def __init__(self, source='VCI', pool_size=5):
        self.source = source
        self.pool = Queue(maxsize=pool_size)
        for _ in range(pool_size):
            self.pool.put(Quote(source=source))
    
    def get_quote(self, symbol):
        quote = self.pool.get()
        quote.symbol = symbol
        return quote
    
    def return_quote(self, quote):
        self.pool.put(quote)
    
    def fetch_history(self, symbol, start, end):
        quote = self.get_quote(symbol)
        try:
            df = quote.history(start=start, end=end)
            return df
        finally:
            self.return_quote(quote)

# Usage
pool = QuotePool(source='VCI', pool_size=3)
df = pool.fetch_history('VCI', '2024-01-01', '2024-12-31')
```

## Logging Setup

```python
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('vnstock.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def fetch_with_logging(symbol, start, end):
    from vnstock import Quote
    
    logger.info(f"Fetching {symbol} from {start} to {end}")
    try:
        quote = Quote(source='VCI', symbol=symbol)
        df = quote.history(start=start, end=end)
        logger.info(f"Success: {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Failed: {e}", exc_info=True)
        raise
```

## Performance Monitoring Decorator

```python
import time
import logging

logger = logging.getLogger(__name__)

def monitor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f"{func.__name__}: {elapsed:.2f}s")
        if elapsed > 5:
            logger.warning(f"{func.__name__} slow: {elapsed:.2f}s")
        return result
    return wrapper

@monitor
def fetch_data(symbol):
    from vnstock import Quote
    quote = Quote(source='VCI', symbol=symbol)
    return quote.history(start='2024-01-01', end='2024-12-31')
```

## Combined Pattern: Resilient Fetcher

```python
from tenacity import retry, stop_after_attempt, wait_exponential
import requests

class ResilientQuoteFetcher:
    def __init__(self):
        self.circuit = CircuitBreaker(failure_threshold=3, timeout_seconds=60)
        self.cache = QuoteCache(ttl_hours=24)
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
    def _fetch(self, symbol, start, end):
        from vnstock import Quote
        quote = Quote(source='VCI', symbol=symbol)
        return quote.history(start=start, end=end)
    
    def get(self, symbol, start, end, use_cache=True):
        if use_cache:
            try:
                return self.cache.get(symbol, start, end)
            except:
                pass
        
        return self.circuit.call(self._fetch, symbol, start, end)
```
