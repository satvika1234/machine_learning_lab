A=[]
n=int(input("enter the size of the square matrix: "))
for i in range(n):
    row=[]
    for j in range(n):
        e=int(input("Enter element: "))
        row.append(e)
    A.append(row)
m=int(input("enter a positive integer: "))
def multiply(X, Y):
    result = [[0]*n for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += X[i][k] * Y[k][j]
    return result
r = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    r.append(row)
for i in range(m):
    r=multiply(r, A)

for i in r:
    print(i)