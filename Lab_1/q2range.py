l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter element: ")))
if len(l)>=3:
    print("Range of the list is:", max(l)-min(l))
else:
    print("List shouldhave at least 3 elements to find the range.")
