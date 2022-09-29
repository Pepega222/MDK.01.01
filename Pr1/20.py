numbers=[float(i) for i in range(7,21)]
mapped_numbers = list(map(lambda x: x%7, numbers))
print(mapped_numbers)
