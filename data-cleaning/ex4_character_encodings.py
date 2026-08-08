"""
Exercise 4: Character Encodings
Dataset: Fatal Police Shootings in the US
Course: Kaggle - Data Cleaning
"""

import pandas as pd
import numpy as np
import charset_normalizer
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

np.random.seed(0)

# ---------------------------------------------------------------------------
# 1) What are encodings?
# ---------------------------------------------------------------------------
sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

# The bytes above were encoded with "big5-tw" (a Chinese-language encoding),
# not standard UTF-8. Decode with the correct encoding, then re-encode to
# UTF-8 (the modern default).
before = sample_entry.decode("big5-tw")
new_entry = before.encode()

# ---------------------------------------------------------------------------
# 2) Reading in files with encoding problems
# ---------------------------------------------------------------------------
filepath = "../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv"

with open(filepath, 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))
print(result)

police_killings = pd.read_csv(filepath, encoding=result['encoding'])

# ---------------------------------------------------------------------------
# 3) Saving files with UTF-8 encoding
# ---------------------------------------------------------------------------
# pandas' to_csv() defaults to UTF-8, so no extra encoding argument is
# required to write the file back out in the modern standard encoding.
police_killings.to_csv("my_file.csv")
