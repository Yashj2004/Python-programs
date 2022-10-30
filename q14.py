a=int(input("enter marks in maths"))
b=int(input("enter marks in english"))
c=int(input("enter marks in science"))
d=int((a+b+c)/3)
if (d>40):
    print("passed")
elif (a>33) and (b>33) and (c>33) :
    print("passed")
else :
    print("failed")
