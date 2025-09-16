# Data Cleaning & Deduplication in Python

## Project Overview
This project demonstrates how to clean a dataset by identifying and removing duplicate records using Python. Ensuring data accuracy and consistency is critical for any data analysis workflow.

## Problem Statement
The dataset contained duplicate entries, which could lead to incorrect analysis. The goal was to:
1. Identify duplicate records.
<img width="957" height="364" alt="image" src="https://github.com/user-attachments/assets/538422f6-49e7-4e13-8de0-96e1b6a39f91" />

2. Remove duplicates while keeping one unique record.
USE df_cleaned = df.drop_duplicates()

3. Save the cleaned dataset.
<img width="957" height="335" alt="image" src="https://github.com/user-attachments/assets/851e4383-8885-4827-a28b-b53c24b84754" />


## Solution Approach

### Step 1: Load the Dataset
```python
import pandas as pd

# Load dataset
df = pd.read_excel('dataset.xlsx')
print("Original Data:")
print(df)

Step 2: Identify Duplicates
# Find duplicate rows
duplicates = df[df.duplicated()]
print("Duplicate rows:")
print(duplicates)


Step 3: Remove Duplicates
# Drop duplicate rows and keep the first occurrence
df_cleaned = df.drop_duplicates()
print("Data after removing duplicates:")
print(df_cleaned)


Step 4: Save Cleaned Data
# Save cleaned dataset to a new file
df_cleaned.to_excel('cleaned_dataset.xlsx', index=False)
print("Cleaned dataset saved as 'cleaned_dataset.xlsx'.")
