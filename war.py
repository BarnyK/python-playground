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
C_SUITS = ['D','H','C','S']
C_FACES = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

class card():
    #klasa karty, posiada informacje o nazwie i wartości karty
    def __init__(self,name):
        self.n = name
        if name[0] in '1JQKA':
            self.val = C_VALS[name[0]]
        else:
            self.val = int(name[0])

    def value(self):
        #oddaje wartość karty
        return self.val

    def name(self):
        #oddaje nazwe karty
        return self.n


class deck():
    def __init__(self, empty=False):
        #tworzy talie kart, przyjmuje True/False czy ma być pusta czy nie
        self.cards = []
        if(empty==False):
            self.cards = [card(x+y) for y in C_SUITS for x in C_FACES]

    def __repr__(self):
        #oddaje liste kart jako string
        return ', '.join([c.name() for c in self.cards])

    def lists(self):
        #oddaje liste kart w talii jako liste
        return self.cards

    def shuffles(self):
        #tasuje karty
        shuffle(self.cards)

    def give(self):
        #oddaje karte z wierzchu
        try:
            return self.cards.pop(0)
        except:
            print('pusto')

    def add(self, *elems):
        #dodaje karte na spod
        for elem in elems:
            self.cards.append(elem)

    def count(self):
        #oddaje ilość kart
        return len(self.cards)

    def isEmpty(self):
        #sprawdza czy pusta
        if self.cards:
            return False
        else:
            return True


def fight(card_a,card_b):
    #funkcja porównująca karty i wywołująca wojnę
    #temu kto wygrał daje karty ze stołu
    if card_a.value()>card_b.value():
        for c in t_a.lists():
            a.add(t_a.give())
        for c in t_b.lists():
            a.add(t_b.give())
        return True
    elif card_b.value()>card_a.value():
        for c in t_a.lists():
            b.add(t_a.give())
        for c in t_b.lists():
            b.add(t_b.give())
        return True
    else:
        #wywołuje wojne i sprawdza czy odda True czy False
        #false oznacza, że któryś z graczy nie ma kart do 'wojny'
        #więc oddaje False by skończy gre i ogłosić remis
        if war():
            return True
        else:
            return False


def war():
    #sprwdza czy gracze mają karty potrzebne do zagrania 'wojny'
    #jeśli mają to wykonuje akcje 'wojny', oddaje False jeśli nie mają
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
    
#tworzenie i tasowanie kart
cards = deck()
cards.shuffles()

#tworzenie pustych talii dla graczy oraz dla kart wyłożonych na stół
a = deck(empty=True)
b = deck(empty=True)
t_a = deck(empty=True)
t_b = deck(empty=True)

#rozdawanie kart
for x in range(26):
    a.add(cards.give())
    b.add(cards.give())

print('Karty pierwszego: {}'.format(a))
print('Karty drugiego: {}'.format(b))

#rozpoczęcie się pętli z grą, na początku sprawdzane jest czy ktoś nie wygrał w poprzedniej turze
#jeśli tak:  wypisuje kto i przerywa loop oraz wypisuje ilość tur
#jeśli nie: dodaje +1 do ilości tur i wywołuje akcje do gry

tury=0
while True:
    if tury>5000:
        print('Turn overflow')
        break
    if a.isEmpty():
        print('Drugi wygrywa')
        break
    if b.isEmpty():
        print('Pierwszy wygrywa')
        break
    tury+=1
    c_a = a.give()
    t_a.add(c_a)
    c_b = b.give()
    t_b.add(c_b)
    if not fight(c_a,c_b):
        print('Remis')
        break
print(tury)
