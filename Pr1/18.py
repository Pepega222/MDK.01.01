a=[ int(i) for i in range(1,21)]
q=[]
for b in a:
    if b%2 == 0:
        q.append(b**2)
    elif b%2 != 0:
        q.append(b+2)
print(q)
