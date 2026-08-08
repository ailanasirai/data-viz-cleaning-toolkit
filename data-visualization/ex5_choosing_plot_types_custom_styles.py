"""
Exercise 5: Choosing Plot Types and Custom Styles
Dataset: Spotify Streaming Data
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
# Load data
# ---------------------------------------------------------------------------
spotify_filepath = "../input/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# ---------------------------------------------------------------------------
# Try out seaborn styles
# Available: "darkgrid", "whitegrid", "dark", "white", "ticks"
# ---------------------------------------------------------------------------
sns.set_style("dark")

plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
plt.title("Spotify Streaming Data (dark style)")
plt.show()

# Swap the style below to compare themes, e.g.:
# sns.set_style("whitegrid")
