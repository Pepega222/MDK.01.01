from collections import defaultdict
from sys import stdin
 
clients = defaultdict(lambda: defaultdict(int)) #O(n)
for line in stdin.readlines(): # O(n)
    client, thing, value = line.split()
    clients[client][thing] += int(value)
         
for client in sorted(clients):  # O(n^2)
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])

#Сложность алгоритма - O(n) * O(n) * O(n^2) = O(n^4)