l=[2,7,4,1,3,6]
count=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==10:
            count+=1
            print(l[i],l[j])
print(count)