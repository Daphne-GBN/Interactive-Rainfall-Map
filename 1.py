import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\daphn\OneDrive\Documents\Desktop\Desktop\DA_project\Processed_Rainfall_Data.csv")

# Ensure 'year' column exists and is of integer type
df["year"] = df["year"].astype(int)

# Option 1: Select only numeric columns before grouping
numeric_columns = df.select_dtypes(include="number").columns
df_grouped = df[numeric_columns].groupby(df["year"]).mean()

# Plot Annual Rainfall Trend
plt.figure(figsize=(10, 5))
plt.plot(df_grouped.index, df_grouped["jan"], marker="o", linestyle="-", color="b", label="January Rainfall")
plt.plot(df_grouped.index, df_grouped["feb"], marker="s", linestyle="--", color="g", label="February Rainfall")
plt.plot(df_grouped.index, df_grouped["mar"], marker="^", linestyle=":", color="r", label="March Rainfall")

plt.xlabel("Year")
plt.ylabel("Average Rainfall (mm)")
plt.title("Yearly Trend of Monthly Rainfall")
plt.legend()
plt.grid(True)
plt.show()

