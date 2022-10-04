my_file = open("27.txt", "w+")
my_file.write('1 2')
my_file.close()
my_file1 = open("28.txt", "w+")
with open('27.txt') as datfile:
    text = datfile.read()
my_file1.write(str(sum(map(int, text.split(None, 2)[:2]))))
my_file1.close()