import sys

def inverse_writing(fruit):
    index = -1
    while index >= - (len(fruit)) :
        letter = fruit[index]
        print(letter)
        index = index -1

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
print(find('hello', 'l'))
