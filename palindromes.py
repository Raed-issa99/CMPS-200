import sys
string = str(sys.argv[1])



def is_palindromes(string):
    string = string.lower()
    if string == string [::-1]:
        return(True)
    else:
        return(False)

n = sys.argv[1:]
def n_palindromes(n):
    print("The palindromes are:", end = " ")
    for i in n:
        if is_palindromes(i):
            print(i, end = ' ')

n_palindromes(n)
