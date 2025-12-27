# Risk Models Reference

## Expected Returns

### mean_historical_return

```python
mean_historical_return(prices, returns_data=False, compounding=True, frequency=252, log_returns=False)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| prices | pd.DataFrame | required | Adjusted closing prices |
| returns_data | bool | False | Input is returns, not prices |
| compounding | bool | True | Geometric mean if True |
| frequency | int | 252 | Periods per year |
| log_returns | bool | False | Use log returns |

**Returns:** pd.Series (annualized mean return per asset)

### ema_historical_return

```python
ema_historical_return(prices, returns_data=False, compounding=True, frequency=252, span=500, log_returns=False)
```

Additional parameter:
- `span` (int): EMA time-span, default 500 days

### capm_return

```python
capm_return(prices, market_prices=None, returns_data=False, risk_free_rate=0.02, 
            compounding=True, frequency=252, log_returns=False)
```

Formula: R_i = R_f + β_i(E(R_m) - R_f)

Additional parameter:
- `market_prices` (pd.DataFrame): Benchmark prices

## Covariance Models

### sample_cov

```python
sample_cov(prices, returns_data=False, frequency=252, log_returns=False)
```

**Returns:** pd.DataFrame (annualized covariance matrix)

### exp_cov

```python
exp_cov(prices, returns_data=False, frequency=252, span=180, log_returns=False)
```

Exponentially weighted covariance.

### semicovariance

```python
semicovariance(prices, returns_data=False, frequency=252, benchmark=0, log_returns=False)
```

Downside covariance only. Formula:
(1/n) Σ_i Σ_j min(r_i, B) × min(r_j, B)

### CovarianceShrinkage

```python
cs = CovarianceShrinkage(prices, returns_data=False, frequency=252, log_returns=False)
```

**Methods:**

```python
# Ledoit-Wolf shrinkage
cs.ledoit_wolf(shrinkage_target='constant_variance')  # or 'single_factor', 'constant_correlation'

# Oracle Approximating Shrinkage
cs.oracle_approximating()
```

Shrinkage formula: Σ_hat = δF + (1-δ)S

Where:
- δ = shrinkage constant
- F = shrinkage target
- S = sample covariance

## Utility Functions

### returns_from_prices

```python
returns_from_prices(prices, log_returns=False)
```

**Returns:** pd.DataFrame (daily returns)

### prices_from_returns

```python
prices_from_returns(returns, log_returns=False)
```

**Returns:** pd.DataFrame (pseudo-prices)

### cov_to_corr / corr_to_cov

```python
cov_to_corr(cov_matrix)  # → correlation matrix
corr_to_cov(corr_matrix, stdevs)  # → covariance matrix
```

### fix_nonpositive_semidefinite

```python
fix_nonpositive_semidefinite(matrix, fix_method='spectral')  # or 'diag'
```

Fix non-PSD matrices for optimization.
