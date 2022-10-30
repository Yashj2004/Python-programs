a=int(input("enter the number"))
f=0
for i in range(2,a):
    if a%i==0:
        print("non prime")
        f=1
        break
       
if f==0:
    print("prime")

