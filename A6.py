import pandas as pd
import numpy as np

def load_thyroid_data(filepath):
    return pd.read_excel(filepath, sheet_name="thyroid0387_UCI")

def get_complete_vectors(df):
    # Select only numeric columns for cosine similarity
    numeric_df = df.select_dtypes(include=np.number)
    v1 = numeric_df.iloc[0].values
    v2 = numeric_df.iloc[1].values
    return v1, v2

def cosine_similarity(v1, v2):
    numerator = np.dot(v1, v2)
    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    return numerator / denominator if denominator != 0 else 0

def main():
    filepath = "Lab Session Data.xlsx"
    df = load_thyroid_data(filepath)

    v1, v2 = get_complete_vectors(df)
    cos_sim = cosine_similarity(v1, v2)

    print("Cosine Similarity between the two observations:", cos_sim)

if __name__ == "__main__":
    main()
