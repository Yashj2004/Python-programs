a="print every word in a sentence that has an even number of letter "
s=a.split(" ")
for i in s:
    if len(i)%2==0:
        print("even")