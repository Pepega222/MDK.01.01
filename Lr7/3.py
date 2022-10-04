with open('27.txt') as t:
    print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')