"""
Exercise 6: Final Project (self-selected dataset)
Dataset: Data Science Job Salaries (Kaggle - ruchi798)
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
# Step 2/3: locate and load the self-selected dataset
# ---------------------------------------------------------------------------
my_filepath = "../input/datasets/ruchi798/data-science-job-salaries/ds_salaries.csv"
my_data = pd.read_csv(my_filepath)
print(my_data.head())

# ---------------------------------------------------------------------------
# Step 4: visualize -- top 10 highest-paying data roles
# ---------------------------------------------------------------------------
top_jobs = (
    my_data.groupby('job_title')['salary_in_usd']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 8))
sns.barplot(x=top_jobs.values, y=top_jobs.index)
plt.title("Top 10 Highest-Paying Data Roles (avg. salary in USD)")
plt.xlabel("Average Salary (USD)")
plt.ylabel("Job Title")
plt.show()
