a=(input("enter the number"))
b=(input("enter the number"))
c=(input("enter the number"))
d=(input("enter the number"))

if (a>b) and (a>c) and (a>d):
    print(a)
elif (b>a) and(b>c) and(b>d):
    print(b)
elif (c>b)and (c>a) and(c>d):
    print(c)
elif (d>b) and(d>c) and(a<d):
    print(d)
else:
        print(a+b+c+d)
