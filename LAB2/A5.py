import pandas as pd
import numpy as np

def load_thyroid_data(filepath):
    return pd.read_excel(filepath, sheet_name="thyroid0387_UCI")

def extract_binary_vectors(df):
    # Select columns that contain ONLY 0 and 1
    binary_cols = [
        col for col in df.columns
        if set(df[col].dropna().unique()).issubset({0, 1})
    ]

    binary_df = df[binary_cols]

    v1 = binary_df.iloc[0].values
    v2 = binary_df.iloc[1].values

    return v1, v2

def compute_frequencies(v1, v2):
    f11 = np.sum((v1 == 1) & (v2 == 1))
    f10 = np.sum((v1 == 1) & (v2 == 0))
    f01 = np.sum((v1 == 0) & (v2 == 1))
    f00 = np.sum((v1 == 0) & (v2 == 0))
    return f11, f10, f01, f00

def jaccard_coefficient(f11, f10, f01):
    denom = f11 + f10 + f01
    return f11 / denom if denom != 0 else 0

def simple_matching_coefficient(f11, f10, f01, f00):
    denom = f11 + f10 + f01 + f00
    return (f11 + f00) / denom if denom != 0 else 0

def main():
    filepath = "Lab Session Data.xlsx"
    df = load_thyroid_data(filepath)

    v1, v2 = extract_binary_vectors(df)
    f11, f10, f01, f00 = compute_frequencies(v1, v2)

    jc = jaccard_coefficient(f11, f10, f01)
    smc = simple_matching_coefficient(f11, f10, f01, f00)

    print("f11:", f11)
    print("f10:", f10)
    print("f01:", f01)
    print("f00:", f00)
    print("Jaccard Coefficient (JC):", jc)
    print("Simple Matching Coefficient (SMC):", smc)

if __name__ == "__main__":
    main()

