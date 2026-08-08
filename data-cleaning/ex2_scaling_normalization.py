"""
Exercise 2: Scaling and Normalization
Dataset: Kickstarter Campaigns (2017)
Course: Kaggle - Data Cleaning
"""

import pandas as pd
import numpy as np
from scipy import stats
from mlxtend.preprocessing import minmax_scaling
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
kickstarters_2017 = pd.read_csv("../input/kickstarter-projects/ks-projects-201801.csv")
np.random.seed(0)

# ---------------------------------------------------------------------------
# Example: scale the "usd_goal_real" column to a 0-1 range
# ---------------------------------------------------------------------------
original_data = pd.DataFrame(kickstarters_2017.usd_goal_real)
scaled_data = minmax_scaling(original_data, columns=['usd_goal_real'])

print('Original data - min:', float(original_data.min()), 'max:', float(original_data.max()))
print('Scaled data   - min:', float(scaled_data.min()), 'max:', float(scaled_data.max()))

# ---------------------------------------------------------------------------
# 1) Practice scaling: the "goal" column
# ---------------------------------------------------------------------------
original_goal_data = pd.DataFrame(kickstarters_2017.goal)
scaled_goal_data = minmax_scaling(original_goal_data, columns=['goal'])

# ---------------------------------------------------------------------------
# 2) Practice normalization: "usd_pledged_real" (given) vs "pledged" (practice)
# ---------------------------------------------------------------------------
# Given example -- normalize usd_pledged_real with a Box-Cox transform
index_of_positive_pledges = kickstarters_2017.usd_pledged_real > 0
positive_pledges = kickstarters_2017.usd_pledged_real.loc[index_of_positive_pledges]

normalized_pledges = pd.Series(
    stats.boxcox(positive_pledges)[0],
    name='usd_pledged_real',
    index=positive_pledges.index
)

ax = sns.histplot(normalized_pledges, kde=True)
ax.set_title("Normalized usd_pledged_real")
plt.show()

# Practice: repeat the same process for the raw "pledged" column
index_of_positive_pledges_raw = kickstarters_2017.pledged > 0
positive_pledges_raw = kickstarters_2017.pledged.loc[index_of_positive_pledges_raw]

normalized_pledges_raw = pd.Series(
    stats.boxcox(positive_pledges_raw)[0],
    name='pledged',
    index=positive_pledges_raw.index
)

ax = sns.histplot(normalized_pledges_raw, kde=True)
ax.set_title("Normalized pledged")
plt.show()

# Conclusion: the two normalized distributions have almost the same shape.
# Currency conversion (pledged -> usd_pledged_real) changes the scale of the
# numbers, but does not change the underlying skew of the distribution.
