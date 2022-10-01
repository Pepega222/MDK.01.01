def sumNums(num):
    sum = 0
    for dig in num:
        sum += int(dig)
    return sum
 
for num in range(100000, 999999):
    num = str(num)
    if sumNums(num[:3]) == sumNums(num[3:]):
        print(num)