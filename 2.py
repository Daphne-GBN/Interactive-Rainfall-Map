import pandas as pd

df = pd.read_csv("Rainfall_Data_Cleaned.csv")

# Print column names (check for unexpected spaces)
print(df.columns.tolist())

