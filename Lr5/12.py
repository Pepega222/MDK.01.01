numbers=[int(i) for i in range(1,100)]
mapped_numbers = list(filter(lambda x: x % 7 == 0,map(int, numbers)))
print(mapped_numbers)
