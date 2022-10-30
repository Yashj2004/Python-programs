def maximum(a,b,c):
    if (a>=b)and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    print(largest)

a=28
b=97
c=75
maximum(a,b,c)
