b='''
clown
circus
xqc
trainwreckTV
'''
a=b.split()
c={i: len(i) for i in a}
key_val = c.items()
key_val_list = list(key_val)
kv = max(key_val_list, key=lambda i : i[1])
print("Самое длинное слово:",kv[0], "Букв:",kv[1])