import sys
import string

morseAlphabet ={
        'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.',
        'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---',
        'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---',
        'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-',
        'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--',
        'z' : '--..',
        '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....',
        '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.', '0' : '-----',
        '.' : '.-.-.-', ',' : '--..--', ':' : '---...', '?' : '..--..',
        "'" : '.----.', '-' : '-....-', '/' : '-..-.', '@' : '.--.-.', '=' : '-...-',
        ' ' : '/'
        }



def text2morse(msg,dict):
    morsecode = ''
    for char in msg:
        if char in dict:
            morsecode += dict[char] + ' '
        else:
            morsecode += '/'
    return morsecode

def morse2text(code,dict):
    message = ''
    morsec = code.split()
    for c in morsec:
        for i in dict:
            if dict[i] == c:
                message += i

    return message

r = sys.argv[1]
s = sys.argv[2]

if r == 'encode':
    print(text2morse(s,morseAlphabet))
elif r == 'decode':
    print(morse2text(s,morseAlphabet))
