n,f,s = int(input()), int(input()), int(input())
a=[int(i) for i in range(f,100,s)]
if n in a:
    print('Число n:',n, "является членом прогрессии")
else:
    print('Число n:',n, "не является членом прогрессии")