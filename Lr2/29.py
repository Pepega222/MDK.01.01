n = int(input())
x = n % 10 + n // 100 * 10 + n % 100 // 10 * 100
print(x)

