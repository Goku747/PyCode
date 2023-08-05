st = "ABF45XA65W2"
lt = set(st)
num = []
ch = []
for i in lt:
    if i.isdigit():
        num.append(i)
    else:
        ch.append(i)
print(''.join(num))
print(''.join(ch))
