f = open("text1.txt", "r")
print(f.readlines(1)[0])
print()
print(f.readlines()[4])
print()
with open("text1.txt", 'r') as f:
    for i in range(5):  print(f.readline(), end='')
print()
with open("text1.txt", 'r') as f:
    for i in range(2): print(f.readline(), end='')
print()
s = open("text1.txt", "r")
print(s.read())