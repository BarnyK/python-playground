#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Another froject from "Introduction to Programming" about September 2017
It's a fully random card game called War
One of my first attempts at objective python
Also need to translate it
"""
from random import shuffle
import time

C_VALS = {'A':14,'K':13,'Q':12,'J':11,'1':10}
C_SUITS_DICT = {"D":"Diamonds", "H":"Hearts", "C":"Clubs", "S":"Spades"}
C_SUITS = ['D','H','C','S']
C_FACES = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class Card():
    """
    Card class contains values of suit and a face of a card
    """
    def __init__(self,name):
        self.n = name
        if name[0] in '1JQKA':
            self.val = C_VALS[name[0]]
        else:
            self.val = int(name[0])

    def value(self):
        # Returns value of a card
        return self.val

    def name(self):
        # Returns a name of a card
        return self.n

    def __repr__(self):
        return self.n

    def __str__(self):
        return "{} of {}".format(self.val,C_SUITS_DICT[self.n[-1]]) 


class Deck():
    def __init__(self, empty=False):
        # Creates a deck of cards, empty or full 
        self.cards = []
        if(empty==False):
            self.cards = [Card(x+y) for y in C_SUITS for x in C_FACES]

    def __repr__(self):
        return ', '.join([c.__repr__() for c in self.cards])


    def shuffles(self):
        # Shuffles the deck of card
        shuffle(self.cards)

    def give(self):
        # Returns a card from the front
        try:
            return self.cards.pop(0)
        except:
            print('Empty')

    def add(self, *elems):
        # Adds a card to the bottom
        for elem in elems:
            self.cards.append(elem)

    def count(self):
        # Returns a count of cards
        return len(self.cards)

    def isEmpty(self):
        # Returns true if no cards 
        if self.cards:
            return False
        else:
            return True


def fight(card_a,card_b):
    # Function compares cards and initiates a war
    # Whoever wins gets cards from table
    if card_a.value()>card_b.value():
        for c in t_a.cards:
            a.add(t_a.give())
        for c in t_b.cards:
            a.add(t_b.give())
        return True
    
    elif card_b.value()>card_a.value():
        for c in t_a.cards:
            b.add(t_a.give())
        for c in t_b.cards:
            b.add(t_b.give())
        return True
    else:
        # Initiates war and checks if it return true or false
        # If a player doesn't have enough cards for war
        # it returns a code for draw
        if war():
            return True
        else:
            return False


def war():
    # Checks if players have enough cards for war
    # If they have it initates war actions
    if a.count()>4 and b.count()>4:
        for x in range(4):
            ca = a.give()
            t_a.add(ca)
            cb = b.give()
            t_b.add(cb)
        if fight(ca,cb):
            return True
        else:
            return False
    else:
        return False

def main():
    # Creation of main deck of cards
    cards = Deck()
    cards.shuffles()

    # Creation of player decks and table stacks
    a = Deck(empty=True)
    b = Deck(empty=True)
    t_a = Deck(empty=True)
    t_b = Deck(empty=True)

    # Dealing the cards
    for x in range(26):
        a.add(cards.give())
        b.add(cards.give())


    print('Karty pierwszego: {}'.format(a))
    print('Karty drugiego: {}'.format(b))

    # Start of game loop, first checks if the games wasn't won already
    # If it was, says who won and how many turns it took
    # If it wasn't, the game still loops

    turns=0
    while True:
        if turns>5000:
            print('Turn overflow')
            break
        if a.isEmpty():
            print('Second player won')
            break
        if b.isEmpty():
            print('First player won')
            break
        turns+=1
        c_a = a.give()
        t_a.add(c_a)
        
        c_b = b.give()
        t_b.add(c_b)
        
        if not fight(c_a,c_b):
            print('Draw')
            break
    print(turns)

if __name__ == "__main__":
    main()
