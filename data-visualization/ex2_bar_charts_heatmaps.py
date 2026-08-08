"""
Exercise 2: Bar Charts and Heatmaps
Dataset: IGN Game Reviews
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
ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
print(ign_data)

# ---------------------------------------------------------------------------
# Q1: highest average Racing score for PC / lowest genre for PS Vita
# (read directly from the printed table above)
# ---------------------------------------------------------------------------
high_score = 7.759930   # PC's highest genre score (Puzzle)
worst_genre = 'Simulation'  # PS Vita's lowest-scoring genre

# ---------------------------------------------------------------------------
# Q3A: bar chart -- average Racing score by platform
# ---------------------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.barplot(x=ign_data.index, y=ign_data['Racing'])
plt.xticks(rotation=90)
plt.title("Average Racing Game Score, by Platform")
plt.show()
# Wii's Racing average (7.41) sits below several competitors, including
# PlayStation (7.91) and Xbox One (8.29).

# ---------------------------------------------------------------------------
# Q4A: heatmap -- every genre against every platform
# ---------------------------------------------------------------------------
plt.figure(figsize=(10, 10))
sns.heatmap(data=ign_data, annot=True)
plt.title("Average Game Score, by Platform and Genre")
plt.show()
# Highest combination in the dataset: PlayStation 4 / Shooter (9.25)
# Lowest combination: Game Boy Color / Fighting & Simulation (4.5 each)
