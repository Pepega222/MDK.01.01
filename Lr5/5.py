a=[1,2,3,4,5,6,7,8,9,10]
def f1(a):
    sum=0
    print(min(a))
    for i in a:
        if i%2 == 0:
            sum+=i
    print(sum)
    quit()
print(f1(a))