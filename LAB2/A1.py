import pandas as pd

df = pd.read_excel('purchase_data.xlsx')

# separate X and y
X = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']]
y = df['Payment (Rs)']

# print(X)
# print(y)
#calculating rank 
import numpy as np
x_val=X.values
y_val=y.values
rank_x= np.linalg.matrix_rank(x_val)
print("Rank of the feature matrix is", rank_x)

#inver and cost calculation
X_pinv = np.linalg.pinv(x_val)
cost = X_pinv @ y_val
print("cost:", cost)





