def fibonacci(n):
    fibonacci = []
    a = 0
    b = 1

    for i in range(0,n):
        fibonacci.append(a)
        c=a+b
        a=b
        b=c
    return fibonacci

print(fibonacci(7))
