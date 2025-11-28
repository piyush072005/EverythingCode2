"""
pandas_examples.py

Small collection of pandas examples demonstrating:
- DataFrame creation (from dict/list)
- Basic selection and filtering
- GroupBy aggregation
- Merge
- Handling missing data
- Simple CSV write/read

Run with: `python python\pandas_examples.py`
"""

import pandas as pd
import numpy as np
import tempfile
import os


def create_from_dict():
    data = {
        "A": [1, 2, 3, 4],
        "B": [5, 6, 7, 8],
        "C": ["x", "y", "z", "x"],
    }
    df = pd.DataFrame(data)
    print("\n[create_from_dict] DataFrame:")
    print(df)
    return df


def create_from_list():
    rows = [["alice", 25, "NY"], ["bob", 30, "CA"], ["cara", 22, "TX"]]
    df = pd.DataFrame(rows, columns=["name", "age", "state"])
    print("\n[create_from_list] DataFrame:")
    print(df)
    return df


def selection_and_filtering(df):
    print("\n[selection_and_filtering] head and column selection:")
    print(df.head())
    if "age" in df.columns:
        print("\nFilter where age > 23:")
        print(df[df["age"] > 23])


def groupby_example():
    df = pd.DataFrame({
        "team": ["A", "A", "B", "B", "B"],
        "points": [10, 15, 10, 5, 20],
    })
    print("\n[groupby_example] source:")
    print(df)
    g = df.groupby("team").sum()
    print("\n[groupby_example] groupby sum:")
    print(g)
    return g


def merge_example():
    left = pd.DataFrame({"key": [1, 2, 3], "left_val": ["L1", "L2", "L3"]})
    right = pd.DataFrame({"key": [2, 3, 4], "right_val": ["R2", "R3", "R4"]})
    print("\n[merge_example] left:")
    print(left)
    print("\n[merge_example] right:")
    print(right)
    merged = left.merge(right, on="key", how="outer")
    print("\n[merge_example] merged (outer):")
    print(merged)
    return merged


def missing_data_example():
    df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, None]})
    print("\n[missing_data_example] original:")
    print(df)
    print("\nDrop rows with any NA:")
    print(df.dropna())
    print("\nFill NA with 0:")
    print(df.fillna(0))
    return df


def csv_io_example():
    df = pd.DataFrame({"x": np.arange(5), "y": np.random.rand(5)})
    out_path = os.path.join(os.getcwd(), "pandas_examples_output.csv")
    df.to_csv(out_path, index=False)
    print(f"\n[csv_io_example] wrote CSV to: {out_path}")
    read = pd.read_csv(out_path)
    print("Read back:")
    print(read)
    return out_path


if __name__ == "__main__":
    print("Pandas examples — running demo")
    d1 = create_from_dict()
    d2 = create_from_list()
    selection_and_filtering(d2)
    groupby_example()
    merge_example()
    missing_data_example()
    csv_io_example()
    print("\nDemo complete.")
