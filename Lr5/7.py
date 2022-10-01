def isPrime(a):
    return all(a % i for i in range(2, a))
print('Число простое' if isPrime(a=int(input())) == True else 'Число не является простым')

