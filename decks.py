import random


def deck():
    DeckOfCards = []
    for j in range(4):
        if j == 0:
            j = 'of Hearts'
        elif j == 1:
            j = 'of Diamonds'
        elif j == 2:
            j = 'of Spades'
        elif j == 3:
            j = 'of Clubs'
        for i in range (1,14):
            if i == 1:
                i = 'Ace '
            elif 2 <= i <= 10:
                i = str(i) + ' '
            elif i == 11:
                i = 'Jack '
            elif i == 12:
                i = 'Queen '
            elif i == 13:
                i = 'King '
            DeckOfCards += [str(i) + (j)]
    return DeckOfCards


DeckOfCards = deck()

def choose_cards(n):
    RandomCards = []
    for i in range(n):
        Card = random.choice(DeckOfCards)
        RandomCards += [Card]
    return RandomCards

def shuffle(list):
    n = len(list)
    for i in range(n):
        r = random.randint(i, n-1)
        x = list[i]
        list[i] = list[r]
        list[r] = x


def draw_cards(n):
    shuffle(DeckOfCards)
    return(DeckOfCards[:n])


def suit_count(hand):
    Spades = 0
    Hearts = 0
    Diamonds = 0
    Clubs = 0
    for i in hand:
        if 'Spades' in i:
            Spades += 1
        elif 'Hearts' in i:
            Hearts += 1
        elif 'Diamonds' in i:
            Diamonds += 1
        elif 'Clubs' in i:
            Clubs += 1
    return([Spades, Hearts, Diamonds, Clubs])

print(deck())
