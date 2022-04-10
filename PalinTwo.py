import sys
string = sys.argv[1]

def palindromes_2(string):
    string = string.lower()
    i = 0
    j = len(string) -1
    palindrome = True
    while j > i and palindrome:
        if string[i] != string[j]:
            palindrome = False
        i += 1
        j -= 1
    return palindrome

print(palindromes_2(string))
