import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("Lab Session Data.xlsx", sheet_name="IRCTC Stock Price")

# Clean column names
df.columns = df.columns.str.strip()

# -----------------------------
# PART 1: Mean & Variance using NumPy
# -----------------------------
price = df['Price']

mean_np = np.mean(price)
var_np = np.var(price)

print("Mean (NumPy):", mean_np)
print("Variance (NumPy):", var_np)

# -----------------------------
# PART 2: Own functions
# -----------------------------
def my_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def my_variance(data):
    m = my_mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return total / len(data)

mean_my = my_mean(price)
var_my = my_variance(price)

print("Mean (My Function):", mean_my)
print("Variance (My Function):", var_my)

# -----------------------------
# PART 3: Computational Complexity
# -----------------------------
def avg_time(func, data, runs=10):
    times = []
    for _ in range(runs):
        start = time.time()
        func(data)
        end = time.time()
        times.append(end - start)
    return sum(times) / runs

print("Avg Time Mean (NumPy):", avg_time(np.mean, price))
print("Avg Time Mean (My):", avg_time(my_mean, price))

print("Avg Time Var (NumPy):", avg_time(np.var, price))
print("Avg Time Var (My):", avg_time(my_variance, price))

# -----------------------------
# PART 4: Wednesday Mean
# -----------------------------
wednesday_price = df[df['Day'] == 'Wed']['Price']
wednesday_mean = wednesday_price.mean()

print("Wednesday Mean:", wednesday_mean)
print("Population Mean:", mean_np)

# -----------------------------
# PART 5: April Mean
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])
april_price = df[df['Date'].dt.month == 4]['Price']
april_mean = april_price.mean()

print("April Mean:", april_mean)
print("Population Mean:", mean_np)

# -----------------------------
# PART 6: Probability of Loss (Chg% < 0)
# -----------------------------
prob_loss = df['Chg%'].apply(lambda x: x < 0).mean()
print("Probability of Loss:", prob_loss)

# -----------------------------
# PART 7: Probability of Profit on Wednesday
# -----------------------------
prob_profit_wed = (
    df[(df['Day'] == 'Wed') & (df['Chg%'] > 0)].shape[0] /
    df[df['Day'] == 'Wed'].shape[0]
)

print("Probability of Profit on Wednesday:", prob_profit_wed)

# -----------------------------
# PART 8: Conditional Probability
# P(Profit | Wednesday)
# -----------------------------
print("Conditional Probability P(Profit | Wednesday):", prob_profit_wed)

# -----------------------------
# PART 9: Scatter Plot (Chg% vs Day)
# -----------------------------
plt.figure()
plt.scatter(df['Day'], df['Chg%'])
plt.xlabel("Day of the Week")
plt.ylabel("Change %")
plt.title("Chg% vs Day of the Week")
plt.show()

