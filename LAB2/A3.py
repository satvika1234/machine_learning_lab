import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Loading Excel file
df = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")
df.columns = df.columns.str.strip()

#Mean & Variance using the NumPy library
price = df['Price']

mean_np = np.mean(price)
var_np = np.var(price)

print("Mean using NumPy:", mean_np)
print("Variance using NumPy:", var_np)

# calculating the mean and variance using own functions
def mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def variance(data):
    m = mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return total / len(data)

m = mean(price)
v = variance(price)

print("Mean:", m)
print("Variance:", v)

# calculating the Computational Complexity

def avg_time(func, data, runs=10):
    times = []
    for _ in range(runs):
        start = time.time()
        func(data)
        end = time.time()
        times.append(end - start)
    return sum(times) / runs

print("Avg Time of Mean using NumPy:", avg_time(np.mean, price))
print("Avg Time of Mean using own fnc:", avg_time(mean, price))

print("Avg Time of Var using NumPy:", avg_time(np.var, price))
print("Avg Time of Var using own fnc:", avg_time(variance, price))

# cakculating the Wednesday Mean

wednesday_price = df[df['Day'] == 'Wed']['Price']
wednesday_mean = wednesday_price.mean()

print("Wednesday Mean:", wednesday_mean)
print("Population Mean:", mean_np)

# April Mean

df['Date'] = pd.to_datetime(df['Date'])
april_price = df[df['Date'].dt.month == 4]['Price']
april_mean = april_price.mean()

print("April Mean:", april_mean)
print("Population Mean:", mean_np)

# Probability of Loss 

prob_loss = df['Chg%'].apply(lambda x: x < 0).mean()
print("Probability of Loss:", prob_loss)

#Probability of Profit on Wednesday

prob_profit_wed = (
    df[(df['Day'] == 'Wed') & (df['Chg%'] > 0)].shape[0] /
    df[df['Day'] == 'Wed'].shape[0]
)

print("Probability of Profit on Wednesday:", prob_profit_wed)


print("Conditional Probability P(Profit | Wednesday):", prob_profit_wed)

# Scatter Plot (Chg% vs Day)

plt.figure()
plt.scatter(df['Day'], df['Chg%'])
plt.xlabel("Day of the Week")
plt.ylabel("Change %")
plt.title("Chg% vs Day of the Week")
plt.show()
