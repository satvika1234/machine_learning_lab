import pandas as pd
import numpy as np

def load_thyroid_data(filepath):
    return pd.read_excel(filepath, sheet_name="thyroid0387_UCI")

def calculate_mean_variance(df):
    numeric_cols = df.select_dtypes(include=np.number)
    mean = numeric_cols.mean()
    variance = numeric_cols.var()   
    return mean, variance

def main():
    filepath = "Lab Session Data.xlsx"
    df = load_thyroid_data(filepath)

    mean, variance = calculate_mean_variance(df)

    print("Mean of numeric variables:\n", mean)
    print("\nVariance of numeric variables:\n", variance)

if __name__ == "__main__":
    main()
