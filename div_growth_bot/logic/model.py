# Prediction Models

# From all the results, predict the top (x) stocks to buy at value

# Only focus on the best value stocks

# Graham Criteria:
# 1. Earnings Growth for last 5 Years
# 2. P/E Ratio < 9
# 3. P/B Ratio < 1.2
# 4. Debt to Asset Ratio < 1.1
# 5. Assets/Liabilities > 1.5

# Rank the stocks for each of the criteria, then average the ranks to get the best stocks
# Select the top (x) stocks to buy

import polars as pl
import jax.numpy as jnp
import sklearn as sk