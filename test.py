
def check(a):
    x = a/2
    while True:
        print (x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

check(20)
