"""
Exercise 3: Scatter Plots
Dataset: Candy Rankings (crowdsourced popularity survey)
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
candy_filepath = "../input/candy.csv"
candy_data = pd.read_csv(candy_filepath, index_col="id")
print(candy_data.head())

# ---------------------------------------------------------------------------
# Q2: compare specific candies directly
# ---------------------------------------------------------------------------
more_popular = '3 Musketeers'   # higher winpercent than Almond Joy
more_sugar = 'Air Heads'        # higher sugarpercent than Baby Ruth

# ---------------------------------------------------------------------------
# Q3: sugar content vs. popularity
# ---------------------------------------------------------------------------
sns.scatterplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
plt.title("Sugar Content vs. Popularity")
plt.show()

sns.regplot(x=candy_data['sugarpercent'], y=candy_data['winpercent'])
plt.title("Sugar Content vs. Popularity (with regression line)")
plt.show()

# ---------------------------------------------------------------------------
# Q5/Q6: price, popularity, and chocolate content together
# ---------------------------------------------------------------------------
sns.scatterplot(x=candy_data['pricepercent'], y=candy_data['winpercent'],
                 hue=candy_data['chocolate'])
plt.title("Price vs. Popularity, colored by Chocolate Content")
plt.show()

sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)
plt.show()

# ---------------------------------------------------------------------------
# Q7: categorical comparison -- chocolate vs. no chocolate
# ---------------------------------------------------------------------------
sns.swarmplot(x=candy_data['chocolate'], y=candy_data['winpercent'])
plt.title("Popularity, Chocolate vs. No Chocolate")
plt.show()
