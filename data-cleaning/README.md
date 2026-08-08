![Python](https://img.shields.io/badge/Python-blue) ![Pandas](https://img.shields.io/badge/Pandas-yellow) ![SciPy](https://img.shields.io/badge/SciPy-orange) ![FuzzyWuzzy](https://img.shields.io/badge/FuzzyWuzzy-green) ![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF)

> Missing data isn't one problem. It's five different problems wearing the same disguise.

Five exercises. Real datasets. From reasoning about *why* a value is missing to fuzzy-matching typo variants of the same country name across thousands of rows.

## Course Completed

| Course | Exercises | Certificate |
|---|---|---|
| [Data Cleaning](https://www.kaggle.com/learn/data-cleaning) | 5 | [🎓 Earned](./certificate.png) |

## Exercise Breakdown

| # | File | Dataset | Problem | Approach |
|---|---|---|---|---|
| 1 | [`ex1_handling_missing_values.py`](./ex1_handling_missing_values.py) | SF Building Permits | Distinguish *why* values are missing (structural vs. never-recorded) | `isnull()` to quantify gaps; `dropna()` to remove; `bfill()` + `fillna(0)` to impute |
| 2 | [`ex2_scaling_normalization.py`](./ex2_scaling_normalization.py) | Kickstarter Campaigns | Prepare skewed numeric columns for modeling | `minmax_scaling()` for range compression; `scipy.stats.boxcox()` for distribution reshaping |
| 3 | [`ex3_parsing_dates.py`](./ex3_parsing_dates.py) | Earthquake Database (1965–2016) | A "Date" column stored as text, with 3 rows in a different format | Compared string lengths to isolate outliers, fixed manually, parsed the rest with `pd.to_datetime()` |
| 4 | [`ex4_character_encodings.py`](./ex4_character_encodings.py) | US Police Killings | A CSV file not encoded in UTF-8 | `charset_normalizer.detect()` on raw bytes to identify the true encoding before loading |
| 5 | [`ex5_inconsistent_data_entry.py`](./ex5_inconsistent_data_entry.py) | Pakistan Intellectual Capital | Same country entered as multiple spellings ("usa" / "usofa") | `str.strip()` + `str.lower()`, then `fuzzywuzzy` similarity scoring to unify near-duplicates |

---

### 1) Handling Missing Values

```python
total_cells = np.prod(sf_permits.shape)
total_missing = sf_permits.isnull().sum().sum()
percent_missing = (total_missing / total_cells) * 100

sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
sf_permits_with_na_imputed = sf_permits.bfill(axis=0).fillna(0)
```
**Insight:** `'Street Number Suffix'` is missing because it structurally doesn't exist for most addresses. `'Zipcode'` is missing because it was never recorded — same blank cell, two different root causes, two different fixes.

### 2) Scaling and Normalization

```python
scaled_goal_data = minmax_scaling(original_goal_data, columns=['goal'])

normalized_pledges = pd.Series(
    stats.boxcox(positive_pledges)[0],
    name='pledged', index=positive_pledges.index
)
```
**Insight:** scaling compresses range; normalization reshapes distribution. Running Box-Cox on both a raw-currency and a USD-converted column produced almost identical shapes — conversion changes the numbers, not the underlying skew.

### 3) Parsing Dates

```python
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"

earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day
```
**Insight:** 3 malformed rows out of tens of thousands were enough to break bulk parsing across the whole column. Found via `.str.len().value_counts()` before applying `pd.to_datetime()`.

### 4) Character Encodings

```python
with open(filepath, 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))

police_killings = pd.read_csv(filepath, encoding=result['encoding'])
police_killings.to_csv("my_file.csv")   # pandas defaults to UTF-8
```
**Insight:** bytes are only readable once decoded with the *correct* encoding — defaulting to UTF-8 on a non-UTF-8 file silently corrupts the text.

### 5) Inconsistent Data Entry

```python
professors['Country'] = professors['Country'].str.lower().str.strip()

def replace_matches_in_column(df, column, string_to_match, min_ratio=47):
    strings = df[column].unique()
    matches = fuzzywuzzy.process.extract(string_to_match, strings, limit=10,
                                         scorer=fuzzywuzzy.fuzz.token_sort_ratio)
    close_matches = [m[0] for m in matches if m[1] >= min_ratio]
    rows_with_matches = df[column].isin(close_matches)
    df.loc[rows_with_matches, column] = string_to_match
```
**Insight:** text cleaning isn't just formatting — it's reconciling the same real-world entity written multiple ways.

## Tech Stack

`Python` · `pandas` · `numpy` · `scipy` · `fuzzywuzzy` · `charset_normalizer` · `Kaggle Notebooks`

## Certificate

![Certificate](./certificate.png)
