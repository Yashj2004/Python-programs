from ctypes.wintypes import WORD


ST="print only the word that start with s in this sentence"
a=ST.split(" ")
for i in a :
    if i[0] == 's':
        print(i)