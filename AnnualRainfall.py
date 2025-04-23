import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv(r"C:\Users\daphn\OneDrive\Documents\Desktop\Desktop\DA_project\Processed_Rainfall_Data.csv")

# Ensure required columns exist
required_columns = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
assert all(col in df.columns for col in required_columns), "Dataset missing required columns"

# Convert all values to numeric, handling errors
df[required_columns] = df[required_columns].apply(pd.to_numeric, errors='coerce')

# Remove extreme outliers using the IQR method
def remove_outliers(df, cols):
    for col in cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), np.nan, df[col])
    return df

df = remove_outliers(df, required_columns)

# Plot boxplot after outlier removal
plt.figure(figsize=(14, 6))
sns.boxplot(data=df[required_columns], palette="coolwarm")
plt.title("Monthly Rainfall Distribution (After Outlier Removal)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(ticks=range(12), labels=required_columns)
plt.show()

# Plot histogram to analyze rainfall distribution
plt.figure(figsize=(12, 6))
df[required_columns].hist(bins=20, figsize=(12, 8), layout=(3, 4), color='skyblue', edgecolor='black')
plt.suptitle("Rainfall Distribution Across Months", fontsize=14)
plt.show()

# Save cleaned dataset
df.to_csv("Cleaned_Rainfall_Data.csv", index=False)

