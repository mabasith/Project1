def fib(n):
    a, b = 0,1
    while b < n:
        print(b," ")
        a,b = b, a+b
    print()
def fib2(n):
    resul = []
    a,b = 0,1
    while b < n:
        resul.append(b)
        a,b = b, a+b
    return resul 
