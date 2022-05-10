def factorial(n):
    if n == 0:
        return 1
    else:
        repeat = factorial(n-1)
        value = repeat * n
        return value

for i in range(2,11):
    if i % 2 != 0:
        print(factorial(i))
