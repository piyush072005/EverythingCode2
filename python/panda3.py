import pandas as pd
import numpy as np

# ==========================================
# 1. Creating DataFrames
# ==========================================

# From dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['NYC', 'LA', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)
print("\n")

# From list of lists
data_list = [['Alice', 25, 'NYC'],
             ['Bob', 30, 'LA'],
             ['Charlie', 35, 'Chicago']]
df2 = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print("DataFrame from list:")
print(df2)
print("\n")

# ==========================================
# 2. Reading and Writing Data
# ==========================================

# Write to CSV
df.to_csv('sample_data.csv', index=False)
print("Data saved to CSV")

# Read from CSV
df_read = pd.read_csv('sample_data.csv')
print("Data read from CSV:")
print(df_read)
print("\n")

# ==========================================
# 3. Basic DataFrame Information
# ==========================================

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:\n", df.dtypes)
print("\nFirst 2 rows:")
print(df.head(2))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nInfo:")
df.info()
print("\nDescriptive statistics:")
print(df.describe())
print("\n")

# ==========================================
# 4. Selecting Data
# ==========================================

# Select single column
print("Select 'Name' column:")
print(df['Name'])
print("\n")

# Select multiple columns
print("Select multiple columns:")
print(df[['Name', 'Age']])
print("\n")

# Select rows by index
print("First 2 rows:")
print(df[:2])
print("\n")

# Select using loc (by label)
print("Select using loc:")
print(df.loc[0:2, ['Name', 'City']])
print("\n")

# Select using iloc (by position)
print("Select using iloc:")
print(df.iloc[0:2, [0, 2]])
print("\n")

# ==========================================
# 5. Filtering Data
# ==========================================

# Filter rows based on condition
print("People older than 28:")
print(df[df['Age'] > 28])
print("\n")

# Multiple conditions
print("People older than 25 and from NYC or LA:")
print(df[(df['Age'] > 25) & (df['City'].isin(['NYC', 'LA']))])
print("\n")

# ==========================================
# 6. Adding and Modifying Data
# ==========================================

# Add new column
df['Salary'] = [50000, 60000, 70000, 55000]
print("Added Salary column:")
print(df)
print("\n")

# Modify existing column
df['Age'] = df['Age'] + 1
print("Incremented Age by 1:")
print(df)
print("\n")

# ==========================================
# 7. Handling Missing Data
# ==========================================

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})
print("DataFrame with missing values:")
print(df_missing)
print("\n")

# Check for missing values
print("Missing values:")
print(df_missing.isnull())
print("\nCount of missing values:")
print(df_missing.isnull().sum())
print("\n")

# Fill missing values
print("Fill missing with 0:")
print(df_missing.fillna(0))
print("\n")

# Drop rows with missing values
print("Drop rows with any missing values:")
print(df_missing.dropna())
print("\n")

# ==========================================
# 8. Sorting Data
# ==========================================

print("Sort by Age (ascending):")
print(df.sort_values('Age'))
print("\n")

print("Sort by Age (descending):")
print(df.sort_values('Age', ascending=False))
print("\n")

# ==========================================
# 9. Grouping and Aggregation
# ==========================================

# Create sample data for grouping
sales_data = pd.DataFrame({
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['East', 'East', 'West', 'West', 'East', 'West'],
    'Sales': [100, 150, 200, 120, 130, 180]
})
print("Sales data:")
print(sales_data)
print("\n")

# Group by and aggregate
print("Total sales by Product:")
print(sales_data.groupby('Product')['Sales'].sum())
print("\n")

print("Average sales by Region:")
print(sales_data.groupby('Region')['Sales'].mean())
print("\n")

# ==========================================
# 10. Basic Statistics
# ==========================================

print("Mean Age:", df['Age'].mean())
print("Median Age:", df['Age'].median())
print("Max Salary:", df['Salary'].max())
print("Min Salary:", df['Salary'].min())
print("Sum of Salaries:", df['Salary'].sum())
print("\n")

# ==========================================
# 11. Applying Functions
# ==========================================

# Apply function to column
df['Age_Squared'] = df['Age'].apply(lambda x: x**2)
print("Applied square function to Age:")
print(df)
print("\n")

# ==========================================
# 12. Merging DataFrames
# ==========================================

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [85, 90, 95]})