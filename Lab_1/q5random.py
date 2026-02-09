import random
l=[]
for i in range(10):
    l.append(random.randint(1, 10))
mean = sum(l) / len(l)
print("Mean :", mean)
l.sort()

n = len(l)
if n % 2 != 0:
    median = l[n // 2]
else:
    median = (l[n // 2 - 1] + l[n // 2]) / 2

print("Median:", median)
freq = {}
for i in l:
    freq[i] = freq.get(i, 0) + 1

mode = max(freq, key=freq.get)
print("Mode:", mode)
