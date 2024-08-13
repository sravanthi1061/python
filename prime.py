a=int(input('enter a number1'))
flag=0

for i in range(2,a):
    if a%i==0:
        flag+=1
        break

if flag==1:
    print("it not is prime")
else:
    print("  a prime")
    
