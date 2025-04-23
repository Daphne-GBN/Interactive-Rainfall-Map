import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\daphn\OneDrive\Documents\Desktop\Desktop\DA_project\Processed_Rainfall_Data.csv")

# Drop the 'year' column (if present)
if 'year' in df.columns:
    df = df.drop(columns=['year'])

# Plot
plt.figure(figsize=(14, 7))
sns.boxplot(data=df.iloc[:, :12], palette="pastel", linewidth=1.5)
plt.xticks(rotation=45)
plt.yscale("log")  # Log scale to handle extreme values
plt.title("Boxplot of Monthly Rainfall")
plt.ylabel("Rainfall (log scale)")
plt.xlabel("Month")
plt.show()



