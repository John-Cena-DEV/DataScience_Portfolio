import pandas as pd

# Load the dataset
df = pd.read_excel('dataset.xlsx')
print("Original Data:")
print(df)

# Identify duplicates
duplicates = df[df.duplicated()]
print(f"\nNumber of duplicate rows: {len(duplicates)}")
print("Duplicate rows:")
print(duplicates)

# Remove duplicates
df_cleaned = df.drop_duplicates()
print("\nData after removing duplicates:")
print(df_cleaned)

# Save the cleaned dataset
df_cleaned.to_excel('cleaned_dataset.xlsx', index=False)
print("\nCleaned dataset saved as 'cleaned_dataset.xlsx'.")
