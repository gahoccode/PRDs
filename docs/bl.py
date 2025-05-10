import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pypfopt import (
    expected_returns,
    risk_models,
    black_litterman,
    BlackLittermanModel,
    EfficientFrontier,
)

# Load prices from CSV file
filePath = "F:\Data Science\CafeF.SolieuGD.Upto24092024\myport2.csv"
df = pd.read_csv(filePath)
df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
df.set_index(["Date"], inplace=True)
prices = df.dropna()
returns = prices.pct_change().dropna()

# Calculate expected returns and sample covariance matrix
mu = expected_returns.mean_historical_return(prices)
cov_matrix = risk_models.sample_cov(prices)

# Display heatmap for covariance matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cov_matrix, annot=True, cmap="coolwarm")
plt.title("Covariance Matrix Heatmap")
plt.show()

# Black-Litterman Model
# Assuming market cap data is available for the assets
market_caps = {"DHC": 100e9, "FMC": 150e9, "REE": 120e9}

# Calculate market-implied risk aversion using a proxy market index (e.g., SPY)
delta = black_litterman.market_implied_risk_aversion(prices)

# Calculate prior returns based on market cap
prior = black_litterman.market_implied_prior_returns(market_caps, delta, cov_matrix)

# Define views
# Example views:
# 1. 'REE' will outperform 'DHC' by 5%
# 2. 'FMC' will outperform 'REE' by 3%
# 3. 'REE' will increase by 10%
# 4. 'FMC' will increase by 3%
# 5. 'DHC' will decrease by 5%
views = np.array([0.05, 0.03, 0.10, 0.03, -0.05]).reshape(-1, 1)
picking_matrix = np.array(
    [
        [-1, 0, 1],  # REE - DHC
        [0, -1, 1],  # FMC - REE
        [0, 0, 1],  # REE increase by 10%
        [0, 1, 0],  # FMC increase by 3%
        [-1, 0, 0],  # DHC decrease by 5%
    ]
)

# Create Black-Litterman model
bl = BlackLittermanModel(cov_matrix, Q=views, P=picking_matrix, pi=prior, tau=0.05)
bl_returns = bl.bl_returns()

# Use the Black-Litterman adjusted returns in Efficient Frontier
ef = EfficientFrontier(bl_returns, cov_matrix)
weights_bl = ef.max_sharpe()
cleaned_weights_bl = ef.clean_weights()

# Save weights to file
ef.save_weights_to_file("weights.csv")

# Print Black-Litterman optimized weights
print("Black-Litterman Optimized Weights:", cleaned_weights_bl)

# Portfolio performance with Black-Litterman model
bl_expected_return, bl_annual_volatility, bl_sharpe_ratio = ef.portfolio_performance(
    verbose=True
)
