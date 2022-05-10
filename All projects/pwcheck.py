import sys
password = sys.argv[1]


def is_8char(string):
    if len(string) >= 8:
        return True
    else:
        return False

def contains_digit(string):
    digits = '123456789'
    for i in string:
        if i in digits:
            return True
    return False


def contains_upper(string):
    if string.lower() == string:
        return False
    else:
        return True

def contains_lower(string):
    if string.upper() == string:
        return False
    else:
        return True

def contains_non_an(string):
    i = 0
    containsNon = False #The string contains a non numerical or alphabetical charecter
    while i < len(string) and (not containsNon):
        if (ord(string[i]) < 48) or (57 < ord(string[i]) < 97) or (ord(string[i]) > 122): #if ord of character of index i is in range of the non alphabatical and numerical values,containsNon becomes True
            containsNon = True
        i += 1
    return containsNon

def password_check(string):
    if is_8char(string) and contains_digit(string) and contains_upper(string) and contains_lower(string) and contains_non_an(string):
        print('The password is good')
    else:
        print('The password is weak')

password_check(password)
