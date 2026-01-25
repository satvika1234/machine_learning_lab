import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_thyroid_data(filepath):
    return pd.read_excel(filepath, sheet_name="thyroid0387_UCI")

def get_binary_data(df, n=20):
    binary_cols = [
        col for col in df.columns
        if set(df[col].dropna().unique()).issubset({0, 1})
    ]
    return df[binary_cols].iloc[:n].values

def get_numeric_data(df, n=20):
    return df.select_dtypes(include=np.number).iloc[:n].values

def compute_jc_smc(v1, v2):
    f11 = np.sum((v1 == 1) & (v2 == 1))
    f10 = np.sum((v1 == 1) & (v2 == 0))
    f01 = np.sum((v1 == 0) & (v2 == 1))
    f00 = np.sum((v1 == 0) & (v2 == 0))

    jc = f11 / (f11 + f10 + f01) if (f11 + f10 + f01) != 0 else 0
    smc = (f11 + f00) / (f11 + f10 + f01 + f00) if (f11 + f10 + f01 + f00) != 0 else 0

    return jc, smc

def cosine_similarity(v1, v2):
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    return np.dot(v1, v2) / denom if denom != 0 else 0

def similarity_matrices(binary_data, numeric_data):
    n = len(binary_data)
    jc_mat = np.zeros((n, n))
    smc_mat = np.zeros((n, n))
    cos_mat = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            jc, smc = compute_jc_smc(binary_data[i], binary_data[j])
            jc_mat[i, j] = jc
            smc_mat[i, j] = smc
            cos_mat[i, j] = cosine_similarity(numeric_data[i], numeric_data[j])

    return jc_mat, smc_mat, cos_mat

def plot_heatmap(matrix, title):
    sns.heatmap(matrix, annot=True, cmap="coolwarm")
    plt.title(title)
    plt.show()

def main():
    filepath = "Lab Session Data.xlsx"
    df = load_thyroid_data(filepath)

    binary_data = get_binary_data(df)
    numeric_data = get_numeric_data(df)

    jc_mat, smc_mat, cos_mat = similarity_matrices(binary_data, numeric_data)

    plot_heatmap(jc_mat, "Jaccard Coefficient Heatmap")
    plot_heatmap(smc_mat, "Simple Matching Coefficient Heatmap")
    plot_heatmap(cos_mat, "Cosine Similarity Heatmap")

if __name__ == "__main__":
    main()
