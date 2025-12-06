import pandas as pd

# Read the CSV file
while True:
    file_path = input("Enter CSV file path: ")
    try:
        df = pd.read_csv(file_path)
        break
    except FileNotFoundError:
        print("Error: File not found. Please try again.")
    except pd.errors.EmptyDataError:
        print("Error: File is empty or invalid. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask user for column and threshold
while True:
    column_name = input("Enter column name: ")
    if column_name in df.columns:
        break
    else:
        print(f"Error: Column '{column_name}' not found. Available columns: {', '.join(df.columns)}")

while True:
    try:
        threshold = float(input("Enter threshold value: "))
        break
    except ValueError:
        print("Error: Invalid threshold. Please enter a numeric value.")

# Display rows where column value exceeds threshold
try:
    result = df[df[column_name] > threshold]
    
    if result.empty:
        print(f"\nNo rows found where {column_name} exceeds {threshold}.")
    else:
        print("\nRows where", column_name, "exceeds", threshold, ":\n")
        print(result)
except TypeError:
    print(f"Error: Cannot compare values in column '{column_name}' with the threshold. Ensure the column contains numeric data.")
except Exception as e:
     print(f"An unexpected error occurred during processing: {e}")