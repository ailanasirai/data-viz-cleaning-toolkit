"""
Exercise 4: Distributions (Histograms & KDE Plots)
Dataset: Breast Cancer Tumor Diagnostics
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
cancer_filepath = "../input/cancer.csv"
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")
print(cancer_data.head())

# Q2 answers (read directly from the first five rows above)
max_perim = 87.46
mean_radius = 9.504

# ---------------------------------------------------------------------------
# Q3: histograms -- Area (mean), split by Diagnosis
# ---------------------------------------------------------------------------
sns.histplot(data=cancer_data, x='Area (mean)', hue='Diagnosis')
plt.title("Tumor Area (mean), Benign vs. Malignant")
plt.show()

# ---------------------------------------------------------------------------
# Q4: KDE plots -- Radius (worst), split by Diagnosis
# ---------------------------------------------------------------------------
sns.kdeplot(data=cancer_data, x='Radius (worst)', hue='Diagnosis', shade=True)
plt.title("Tumor Radius (worst), Benign vs. Malignant")
plt.show()
