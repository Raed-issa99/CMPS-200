
#Returns a version of the string str without vowels and whose
#characters appear in the same order htey appear in string

def without_vowels(str):
    vowels = "aAeEiIoOuU" #all the vowels
    str_no_vow = ''
    for i in str:
        if i in vowels: #if i is in vowels, ie i is one of the letters of the vowels string, ignore i and move to next i
            continue #i asked the TA if i am allowed to use this and he said yes
        else: str_no_vow += i
    return str_no_vow

#Tests the function without_vowels


#Print values of AUB, cmps200, and Exam 1! when called with the function without_vowels.
print(without_vowels('AUB'),without_vowels('cmps 200'),without_vowels('Exam 1!'))
