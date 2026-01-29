import pandas as pd
import numpy as np


#calculate mean and variance for all numeric variables
def mean_variance(df):
    cols = df.select_dtypes(include=np.number)
    mean = cols.mean()
    variance = cols.var()   
    return mean, variance

def main():
    #loading the excel file
    filepath = "Lab Session Data.xlsx"
    df = pd.read_excel(filepath, sheet_name="thyroid0387_UCI")

    mean, variance = mean_variance(df)

    print("Mean of numeric variables:\n", mean)
    print("\nVariance of numeric variables:\n", variance)

if __name__ == "__main__":
    main()
