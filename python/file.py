import pandas as pd

# Read the CSV file
file_path = input("Enter CSV file path: ")
df = pd.read_csv(file_path)

# Ask user for column and threshold
column_name = input("Enter column name: ")
threshold = float(input("Enter threshold value: "))

# Display rows where column value exceeds threshold
result = df[df[column_name] > threshold]

print("\nRows where", column_name, "exceeds", threshold, ":\n")
print(result)