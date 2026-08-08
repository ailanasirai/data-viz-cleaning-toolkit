"""
Exercise 3: Parsing Dates
Dataset: Earthquake Database (1965-2016)
Course: Kaggle - Data Cleaning
"""

import pandas as pd
import numpy as np
import seaborn as sns
import datetime
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
earthquakes = pd.read_csv("../input/earthquake-database/database.csv")
np.random.seed(0)

# ---------------------------------------------------------------------------
# 1) Check the data type of the "Date" column
# ---------------------------------------------------------------------------
print(earthquakes['Date'].head())
print("dtype:", earthquakes['Date'].dtype)
# The column looks like dates but pandas is reading it as plain text
# (dtype: object) -- it has not been parsed as an actual datetime.

# ---------------------------------------------------------------------------
# 2) Convert the "Date" column to datetime
# ---------------------------------------------------------------------------
# Inspect the known problem row (different format than the rest)
print(earthquakes[3378:3383])

# Check how widespread the formatting issue is by comparing string lengths
date_lengths = earthquakes.Date.str.len()
print(date_lengths.value_counts())

# Locate every row using the non-standard (24-character) format
indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
print(earthquakes.loc[indices])

# Manually correct the malformed rows to the standard MM/DD/YYYY format
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"

# Now the entire column can be parsed with a single consistent format
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")

# ---------------------------------------------------------------------------
# 3) Select the day of the month
# ---------------------------------------------------------------------------
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

# ---------------------------------------------------------------------------
# 4) Plot the day of the month to check the date parsing
# ---------------------------------------------------------------------------
day_of_month_earthquakes = day_of_month_earthquakes.dropna()
sns.histplot(day_of_month_earthquakes, kde=False, bins=31)
# If parsing succeeded, days should be roughly evenly distributed across
# 1-31, with no unnatural spike at any single value.
