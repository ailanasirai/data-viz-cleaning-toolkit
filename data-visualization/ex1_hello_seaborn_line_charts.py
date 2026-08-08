"""
Exercise 1: Hello, Seaborn & Line Charts
Datasets: FIFA Rankings | LA Museum Visitors
Course: Kaggle - Data Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

pd.plotting.register_matplotlib_converters()
warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# ---------------------------------------------------------------------------
# Hello, Seaborn -- FIFA rankings
# ---------------------------------------------------------------------------
fifa_filepath = "../input/fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

plt.figure(figsize=(16, 6))
sns.lineplot(data=fifa_data)
plt.title("FIFA Rankings Over Time")
plt.show()

# ---------------------------------------------------------------------------
# Line Charts -- LA Museum Visitors
# ---------------------------------------------------------------------------
museum_filepath = "../input/museum_visitors.csv"
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

# Q2: review the data
print(museum_data.tail())

# Q2 answers (read directly from the printed table above)
ca_museum_jul18 = 2620
avila_oct18 = 14658  # Avila Adobe (19280) - Firehouse Museum (4622)

# Q3: line chart, all four museums at once
plt.figure(figsize=(14, 6))
sns.lineplot(data=museum_data)
plt.title("Visitors to All Four LA Museums")
plt.show()

# Q4A: isolate a single museum to check for seasonality
plt.figure(figsize=(14, 6))
sns.lineplot(data=museum_data['Avila Adobe'])
plt.title("Avila Adobe Visitors Over Time")
plt.show()
