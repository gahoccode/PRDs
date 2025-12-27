# Optimization Methods Reference

## EfficientFrontier

### Constructor

```python
EfficientFrontier(expected_returns, cov_matrix, weight_bounds=(0, 1), solver=None, verbose=False, solver_options=None)
```

**Parameters:**
- `expected_returns` (pd.Series, list, np.ndarray): Expected returns per asset
- `cov_matrix` (pd.DataFrame, np.array): Covariance matrix
- `weight_bounds` (tuple): Min/max weight per asset, default (0, 1)
- `solver` (str): CVXPY solver name
- `verbose` (bool): Debug output
- `solver_options` (dict): Solver parameters

### Methods

| Method | Parameters | Returns |
|--------|------------|---------|
| `min_volatility()` | None | OrderedDict weights |
| `max_sharpe(risk_free_rate=0.02)` | risk_free_rate: float | OrderedDict weights |
| `max_quadratic_utility(risk_aversion=1, market_neutral=False)` | risk_aversion: float, market_neutral: bool | OrderedDict weights |
| `efficient_risk(target_volatility, market_neutral=False)` | target_volatility: float | OrderedDict weights |
| `efficient_return(target_return, market_neutral=False)` | target_return: float | OrderedDict weights |
| `portfolio_performance(verbose=False, risk_free_rate=0.02)` | verbose: bool | (return, volatility, sharpe) |
| `clean_weights(cutoff=0.0001, rounding=5)` | cutoff: float, rounding: int | OrderedDict weights |
| `add_constraint(constraint)` | constraint: callable | None |
| `add_objective(objective, **kwargs)` | objective: callable | None |

## EfficientSemivariance

Penalizes only downside volatility.

```python
EfficientSemivariance(expected_returns, returns, frequency=252, benchmark=0, weight_bounds=(0, 1))
```

**Methods:**
- `min_semivariance()` → OrderedDict
- `efficient_risk(target_semideviation, market_neutral=False)` → OrderedDict
- `efficient_return(target_return, market_neutral=False)` → OrderedDict

## EfficientCVaR

Conditional Value at Risk optimization.

```python
EfficientCVaR(expected_returns, returns, beta=0.95, weight_bounds=(0, 1))
```

**Methods:**
- `min_cvar()` → OrderedDict
- `efficient_risk(target_cvar, market_neutral=False)` → OrderedDict
- `efficient_return(target_return, market_neutral=False)` → OrderedDict

## EfficientCDaR

Conditional Drawdown at Risk optimization.

```python
EfficientCDaR(expected_returns, returns, beta=0.95, weight_bounds=(0, 1))
```

**Methods:**
- `min_cdar()` → OrderedDict
- `efficient_risk(target_cdar, market_neutral=False)` → OrderedDict
- `efficient_return(target_return, market_neutral=False)` → OrderedDict

## HRPOpt

Hierarchical Risk Parity (no expected returns needed).

```python
HRPOpt(returns)
```

**Methods:**
- `optimize(linkage_method='single')` → OrderedDict
- `portfolio_performance(verbose=False, risk_free_rate=0.02, frequency=252)` → (return, vol, sharpe)

## DiscreteAllocation

Convert weights to share counts.

```python
DiscreteAllocation(weights, latest_prices, total_portfolio_value, short_ratio=0.30)
```

**Methods:**
- `greedy_portfolio(reinvest=False, verbose=False)` → (dict allocation, float leftover)
- `lp_portfolio(reinvest=False, verbose=False, solver='ECOS_BB')` → (dict allocation, float leftover)

## Custom Optimization

```python
from pypfopt.base_optimizer import BaseConvexOptimizer

# Convex objective
ef.convex_objective(custom_objective, weights_sum_to_one=True, **kwargs)

# Non-convex objective
ef.nonconvex_objective(custom_objective, objective_args=None, weights_sum_to_one=True, 
                       constraints=None, solver='SLSQP', initial_guess=None)
```
