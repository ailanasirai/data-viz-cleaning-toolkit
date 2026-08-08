"""
Exercise 1: Handling Missing Values
Dataset: San Francisco Building Permit Applications
Course: Kaggle - Data Cleaning
"""

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
sf_permits = pd.read_csv(
    "../input/building-permit-applications-data/Building_Permits.csv",
    low_memory=False
)
np.random.seed(0)

# ---------------------------------------------------------------------------
# 1) Take a first look at the data
# ---------------------------------------------------------------------------
print(sf_permits.head())
# Observation: the dataset does contain missing values -- multiple columns
# show NaN in the preview above.

# ---------------------------------------------------------------------------
# 2) How many missing data points do we have?
# ---------------------------------------------------------------------------
total_cells = np.prod(sf_permits.shape)
total_missing = sf_permits.isnull().sum().sum()

percent_missing = (total_missing / total_cells) * 100
print(f"Percent of values missing: {percent_missing:.2f}%")

# ---------------------------------------------------------------------------
# 3) Figure out why the data is missing
# ---------------------------------------------------------------------------
# 'Street Number Suffix' -- missing because it structurally does not exist
#   for most addresses (e.g. "123 Main St" has no suffix at all).
# 'Zipcode' -- missing because it was not recorded, since every address
#   has a real zip code that simply wasn't captured.

# ---------------------------------------------------------------------------
# 4) Drop missing values: rows
# ---------------------------------------------------------------------------
rows_after_dropna = sf_permits.dropna()
print(f"Rows remaining after dropping any row with a missing value: {len(rows_after_dropna)}")
# (Original sf_permits is left unmodified -- dropna() returns a new object.)

# ---------------------------------------------------------------------------
# 5) Drop missing values: columns
# ---------------------------------------------------------------------------
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
dropped_columns = sf_permits.shape[1] - sf_permits_with_na_dropped.shape[1]
print(f"Columns dropped: {dropped_columns}")

# ---------------------------------------------------------------------------
# 6) Fill in missing values automatically
# ---------------------------------------------------------------------------
# Replace NaNs with the next valid value in the column (backward fill),
# then replace any values still missing (e.g. trailing NaNs) with 0.
sf_permits_with_na_imputed = sf_permits.bfill(axis=0).fillna(0)
