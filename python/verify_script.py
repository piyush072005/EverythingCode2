import subprocess
import sys
import os

def run_test(name, inputs):
    print(f"--- Running Test: {name} ---")
    try:
        # Run the script using the same python executable
        process = subprocess.Popen(
            [sys.executable, 'python/file.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.getcwd()
        )
        stdout, stderr = process.communicate(input=inputs, timeout=5)
        
        print("STDOUT:")
        print(stdout)
        if stderr:
            print("STDERR:")
            print(stderr)
            
    except subprocess.TimeoutExpired:
        print("Timeout detected!")
        process.kill()
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    # Test 1: Valid Case
    # Input: file, column, threshold
    run_test("Valid Case", "python/test_data.csv\nscore\n80\n")

    # Test 2: Invalid File
    # Input: invalid_file, valid_file, column, threshold
    run_test("Invalid File Recovery", "nonexistent.csv\npython/test_data.csv\nscore\n80\n")

    # Test 3: Invalid Column
    # Input: valid_file, invalid_col, valid_col, threshold
    run_test("Invalid Column Recovery", "python/test_data.csv\nwrong_col\nscore\n80\n")

    # Test 4: Invalid Threshold
    # Input: valid_file, valid_col, invalid_threshold, valid_threshold
    run_test("Invalid Threshold Recovery", "python/test_data.csv\nscore\nabc\n80\n")
