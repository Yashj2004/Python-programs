a=[3,7,0,7,6,5,5,4,9,7,3,8,65,4,5,9,6]
b=list(filter(lambda x:x%2==0,a))
print(b)
c=list(map(lambda x:x%2==0,a))
print(c)
