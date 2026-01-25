#A2
import pandas as pd

df = pd.read_excel('purchase_data.xlsx')



from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df.columns = df.columns.str.strip()
df['Class'] = df['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')

# separate X and y
X = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']]
y = df['Class']

le = LabelEncoder()
y = le.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

#  model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

new = pd.DataFrame(
    [[4, 1, 2]],
    columns=['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']
)

result = model.predict(new)
print(le.inverse_transform(result)[0])
