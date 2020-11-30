a=input()
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
trans=""
for c in a:
    if c in b:
        num = b.find(c)
        num = num - 3
        if num < 0:
            num = num + len(b)
        trans = trans + b[num]
    else:
        trans = trans + c
print(trans)


            
