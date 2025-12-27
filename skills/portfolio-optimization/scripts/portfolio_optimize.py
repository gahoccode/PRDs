#!/usr/bin/env python3
"""
Complete portfolio optimization workflow.

Usage:
    python portfolio_optimize.py prices.csv --value 100000 --method max_sharpe
"""

import argparse
import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier, HRPOpt, plotting
from pypfopt.expected_returns import mean_historical_return, ema_historical_return
from pypfopt.risk_models import sample_cov, CovarianceShrinkage
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices


def load_prices(filepath: str) -> pd.DataFrame:
    """Load price data from CSV. Expects date index and ticker columns."""
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df


def calculate_returns_and_cov(prices: pd.DataFrame, 
                               returns_method: str = "mean",
                               cov_method: str = "sample") -> tuple:
    """Calculate expected returns and covariance matrix."""
    
    # Expected returns
    if returns_method == "mean":
        mu = mean_historical_return(prices)
    elif returns_method == "ema":
        mu = ema_historical_return(prices, span=500)
    else:
        mu = mean_historical_return(prices)
    
    # Covariance
    if cov_method == "sample":
        S = sample_cov(prices)
    elif cov_method == "shrinkage":
        cs = CovarianceShrinkage(prices)
        S = cs.ledoit_wolf()
    else:
        S = sample_cov(prices)
    
    return mu, S


def optimize_portfolio(mu: pd.Series, 
                       S: pd.DataFrame,
                       method: str = "max_sharpe",
                       risk_free_rate: float = 0.02,
                       target: float = None,
                       risk_aversion: float = 1.0) -> dict:
    """Run optimization with specified method."""
    
    ef = EfficientFrontier(mu, S)
    
    if method == "max_sharpe":
        ef.max_sharpe(risk_free_rate=risk_free_rate)
    elif method == "min_vol":
        ef.min_volatility()
    elif method == "max_utility":
        ef.max_quadratic_utility(risk_aversion=risk_aversion)
    elif method == "target_return":
        ef.efficient_return(target_return=target)
    elif method == "target_risk":
        ef.efficient_risk(target_volatility=target)
    
    weights = ef.clean_weights()
    performance = ef.portfolio_performance(risk_free_rate=risk_free_rate)
    
    return {
        "weights": weights,
        "expected_return": performance[0],
        "volatility": performance[1],
        "sharpe_ratio": performance[2]
    }


def optimize_hrp(prices: pd.DataFrame) -> dict:
    """Run Hierarchical Risk Parity optimization."""
    returns = prices.pct_change().dropna()
    hrp = HRPOpt(returns)
    weights = hrp.optimize()
    performance = hrp.portfolio_performance()
    
    return {
        "weights": weights,
        "expected_return": performance[0],
        "volatility": performance[1],
        "sharpe_ratio": performance[2]
    }


def allocate_shares(weights: dict, 
                    prices: pd.DataFrame,
                    total_value: float) -> tuple:
    """Convert weights to share allocation."""
    latest_prices = get_latest_prices(prices)
    da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=total_value)
    allocation, leftover = da.greedy_portfolio()
    return allocation, leftover


def main():
    parser = argparse.ArgumentParser(description="Portfolio Optimization")
    parser.add_argument("prices", help="CSV file with price data")
    parser.add_argument("--value", type=float, default=100000, help="Portfolio value")
    parser.add_argument("--method", default="max_sharpe", 
                        choices=["max_sharpe", "min_vol", "max_utility", 
                                "target_return", "target_risk", "hrp"])
    parser.add_argument("--target", type=float, help="Target for return/risk methods")
    parser.add_argument("--risk-free", type=float, default=0.02, help="Risk-free rate")
    parser.add_argument("--risk-aversion", type=float, default=1.0)
    parser.add_argument("--returns-method", default="mean", choices=["mean", "ema"])
    parser.add_argument("--cov-method", default="shrinkage", choices=["sample", "shrinkage"])
    
    args = parser.parse_args()
    
    # Load data
    prices = load_prices(args.prices)
    print(f"Loaded {len(prices)} days of data for {len(prices.columns)} assets")
    
    # Optimize
    if args.method == "hrp":
        result = optimize_hrp(prices)
    else:
        mu, S = calculate_returns_and_cov(prices, args.returns_method, args.cov_method)
        result = optimize_portfolio(mu, S, args.method, args.risk_free, 
                                   args.target, args.risk_aversion)
    
    # Display results
    print("\n=== Portfolio Performance ===")
    print(f"Expected Return: {result['expected_return']:.2%}")
    print(f"Volatility: {result['volatility']:.2%}")
    print(f"Sharpe Ratio: {result['sharpe_ratio']:.2f}")
    
    print("\n=== Weights ===")
    for ticker, weight in sorted(result['weights'].items(), key=lambda x: -x[1]):
        if weight > 0.001:
            print(f"  {ticker}: {weight:.2%}")
    
    # Allocate shares
    allocation, leftover = allocate_shares(result['weights'], prices, args.value)
    
    print(f"\n=== Share Allocation (${args.value:,.0f}) ===")
    for ticker, shares in sorted(allocation.items(), key=lambda x: -x[1]):
        print(f"  {ticker}: {shares} shares")
    print(f"\nLeftover: ${leftover:.2f}")


if __name__ == "__main__":
    main()
