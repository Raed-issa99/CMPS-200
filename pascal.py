import sys
def generate_pascal(n):
    triangle =[[1], [1,1]]
    for i in range(2,n+1):
        interior = [(triangle[i-1][j]+triangle[i-1][j-1]) for j in range(1,len(triangle[i-1]))]
        line = [1] + interior + [1]
        triangle += [line]
    return triangle

def print_triangle(coeffs):
    for i in coeffs:
        for j in i:
            print(j, end = ' ')
        print()
n = int(sys.argv[1])
print_triangle(generate_pascal(n))
