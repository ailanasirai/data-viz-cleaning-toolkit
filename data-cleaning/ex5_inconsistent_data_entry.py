"""
Exercise 5: Inconsistent Data Entry
Dataset: Pakistan Intellectual Capital
Course: Kaggle - Data Cleaning
"""

import pandas as pd
import numpy as np
import fuzzywuzzy
from fuzzywuzzy import process
import charset_normalizer
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message="Using slow pure-python SequenceMatcher")

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
professors = pd.read_csv("../input/pakistan-intellectual-capital/pakistan_intellectual_capital.csv")
np.random.seed(0)

# ---------------------------------------------------------------------------
# Recap: cleaning done in the tutorial for the "Country" column
# ---------------------------------------------------------------------------
professors['Country'] = professors['Country'].str.lower()
professors['Country'] = professors['Country'].str.strip()

countries = professors['Country'].unique()


def replace_matches_in_column(df, column, string_to_match, min_ratio=47):
    """Replace close fuzzy matches to `string_to_match` with a single
    canonical value, so typo variants of the same real-world entry
    collapse into one consistent label."""
    strings = df[column].unique()
    matches = fuzzywuzzy.process.extract(
        string_to_match, strings, limit=10,
        scorer=fuzzywuzzy.fuzz.token_sort_ratio
    )
    close_matches = [m[0] for m in matches if m[1] >= min_ratio]
    rows_with_matches = df[column].isin(close_matches)
    df.loc[rows_with_matches, column] = string_to_match
    print("All done!")


replace_matches_in_column(df=professors, column='Country', string_to_match="south korea")
countries = professors['Country'].unique()

# ---------------------------------------------------------------------------
# 1) Examine another column: "Graduated from"
# ---------------------------------------------------------------------------
print(professors['Graduated from'].unique())
# Observation: several entries represent the same institution but differ
# only by leading/trailing whitespace (e.g. " Punjab University" vs.
# "Punjab University ").

# ---------------------------------------------------------------------------
# 2) Text pre-processing: strip whitespace
# ---------------------------------------------------------------------------
professors['Graduated from'] = professors['Graduated from'].str.strip()

# ---------------------------------------------------------------------------
# 3) Continue working with countries: unify "usa" and "usofa"
# ---------------------------------------------------------------------------
countries = professors['Country'].unique()
countries.sort()
print(countries)

replace_matches_in_column(df=professors, column='Country', string_to_match="usa", min_ratio=70)
