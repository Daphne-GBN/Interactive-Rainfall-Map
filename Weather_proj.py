import pandas as pd

# Load the processed data
df = pd.read_csv("Processed_Rainfall_Data.csv")

# Display extreme values (highest and lowest rainfall)
print(df.describe())  # Summary stats
print(df[df['jan'] > df['jan'].quantile(0.99)])  # Top 1% outliers in January
print(df[df['jan'] < df['jan'].quantile(0.01)])  # Bottom 1% outliers in January
print(df[df['feb'] > df['feb'].quantile(0.99)])  # Top 1% outliers in February
print(df[df['feb'] < df['feb'].quantile(0.01)])  # Bottom 1% outliers in February

