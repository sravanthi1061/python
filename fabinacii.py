first=0
second=1

count=int(input('enter number of fabinocii series'))
print(first)
print(second)
i=3
while i<=count:
    res=first+second
    print(res)
    first=second
    second=res
    i+=1
    
