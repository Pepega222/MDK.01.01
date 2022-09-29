n=input()
min=n[0]
for i in range(len(n)):
    if int(i) < int(min):
        min = int(i)
min=str(min)
s=0   
for j in n:
    if j == min:
        s+=1
print(s)

