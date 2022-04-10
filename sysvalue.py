import sys

numbers = []
for s in sys.argv[1:]:
    numbers += [int(s)]
print(numbers)


def average(a):
    total = 0.0
    for v in a:
        total += v
    return(total/len(a))

print average(numbers)
