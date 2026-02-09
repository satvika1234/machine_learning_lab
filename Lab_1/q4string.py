s=input("enter a string:")
max_count=0
max_char=s[0]
for i in range(len(s)):
    count=0
    count+=s.count(s[i])
    if count>max_count:
        max_count=count
        max_char=s[i]
print("character:",max_char)
print("count:",max_count)
