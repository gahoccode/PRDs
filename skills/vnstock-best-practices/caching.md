# Caching Patterns for VNStock Quote

## File-Based Cache with TTL

```python
import pickle
import os
from datetime import datetime

class QuoteCache:
    def __init__(self, cache_dir='./cache', ttl_hours=24):
        self.cache_dir = cache_dir
        self.ttl_seconds = ttl_hours * 3600
        os.makedirs(cache_dir, exist_ok=True)
    
    def _cache_path(self, symbol, start, end):
        return f"{self.cache_dir}/VCI_{symbol}_{start}_{end}.pkl"
    
    def _is_valid(self, path):
        if not os.path.exists(path):
            return False
        age = datetime.now().timestamp() - os.path.getmtime(path)
        return age < self.ttl_seconds
    
    def get(self, symbol, start, end):
        from vnstock import Quote
        
        path = self._cache_path(symbol, start, end)
        
        if self._is_valid(path):
            with open(path, 'rb') as f:
                return pickle.load(f)
        
        quote = Quote(source='VCI', symbol=symbol)
        df = quote.history(start=start, end=end)
        
        with open(path, 'wb') as f:
            pickle.dump(df, f)
        
        return df
```

## Usage

```python
cache = QuoteCache(ttl_hours=24)

# First call fetches from API and caches
df = cache.get('VCI', '2024-01-01', '2024-12-31')

# Subsequent calls within 24h return cached data
df = cache.get('VCI', '2024-01-01', '2024-12-31')
```

## Cache Invalidation

```python
def clear_cache(self, symbol=None):
    """Clear all cache or specific symbol"""
    import glob
    pattern = f"{self.cache_dir}/VCI_{symbol or '*'}_*.pkl"
    for f in glob.glob(pattern):
        os.remove(f)
```

## Memory Cache (Session Only)

```python
from functools import lru_cache
from vnstock import Quote

@lru_cache(maxsize=100)
def get_history_cached(symbol, start, end):
    quote = Quote(source='VCI', symbol=symbol)
    return quote.history(start=start, end=end)
```

**Note:** `lru_cache` requires hashable arguments. DataFrames are not cached across sessions.
