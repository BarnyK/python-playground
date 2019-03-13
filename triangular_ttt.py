#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Code that I wrote for a project at "Introduction to Programming" about September 2017
It's a tic-tac-toe on a triangular board with minimax alghoritm
It plays with itself in default settings
Has argparse for soem reason
Documentation and code mostly in polish gonna change that someday
"""

import argparse
import re
from math import inf, ceil
import time

#argumenty do włączania z konsoli
parser = argparse.ArgumentParser()
parser.add_argument('-s','--size',
                    default=4,
                    nargs='?',
                    type=int,
                    help='wielkosc planszy')
parser.add_argument('-l','--line',
                    default=3,
                    nargs='?',
                    type=int,
                    help='dlugosc wygrywajacej linii')
parser.add_argument('-c','--controlled',
                     action='store_false',
                     help='czy kółko ma być kontrolowane przez człowieka')
parser.add_argument('-v','--verbose',
                    action='store_true',
                    help='wypisuje czas')
args = parser.parse_args()
verb = args.verbose

## głębokość do której minimax będzie szukał, -1 ustawia pół ilości pól planszy
## -2 ustawia całą
DEPTH=6
VALUES = {}

def genBoard(size):
    # generuje trójkątną plansze i zwraca ją jako krotke napisów
    # posiada też informacje o ostatnim ruchu
    if size<1:
        raise Exception
    board = []
    for x in range(size,0,-1):
        board.append('.'*x)
    board.extend([(0,0)])
    return tuple(board)

def drawBoard(board):
    #działa
    #rysuje ładnie plansze w konsoli
    for x in board[:-1]: 
        print(x)

def put(board,sign,pos):
    #  stawia znak w podanym miejscu na planszy
    x,y = pos
    newrow = board[x][:y]+sign+board[x][y+1:]
    board = board[:x]+tuple([newrow])+board[x+1:]
    board = list(board[:-1])
    board.extend([pos])
    return tuple(board)

def empty(board):
    #działa
    #zwraca miejsca na planszy nie zajęte przez żaden znak
    empty = []
    board=board[:-1]
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y]=='.':
                empty.append((x,y))
    return empty

def scount(board,sign):
    #oddaje liczbe znaków na planszy
    count = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y]==sign:
                count+=1
    return count

def evaluate(board,sign,k):
    #działa
    #ocenia plansze dla danego znaku
    #zwraca 1 jeśli wygrana dla niego
    #zwraca -1 jeśli dla przeciwnika
    #zwraca 0 jeśli remis
    global VALUES
    if board[:-1] in VALUES.keys():
        if sign=='x':
            return VALUES[board[:-1]]
        else:
            return -VALUES[board[:-1]]
    u,w = czywygrana(board,k)
    if w=='Remis':
        VALUES[board[:-1]]=0
        return 0
    elif not w:
        VALUES[board[:-1]]=0
        return 0
    elif w==sign:
        VALUES[board[:-1]]=1
        return 1
    else:
        VALUES[board[:-1]]=-1
        return -1

def minimax(board, depth, player, K):
    if scount(board,'o')==scount(board,'x'):
        sign = 'o'
    else:
        sign = 'x'
    win, side = czywygrana(board,K)
    if depth==0 or win:
        return (-1,-1,evaluate(board,sign,K))
    if player=='MAX':
        bestValue = (-1,-1,-inf)
        for emp in empty(board):
            newboard = put(board,sign,emp)
            x = (emp[0],emp[1],minimax(newboard,depth-1,'MIN',K)[2])
            if bestValue[2]<x[2]:
                bestValue=x
        return bestValue
    else:
        bestValue = (-1,-1,+inf)
        for emp in empty(board):
            newboard = put(board,sign,emp)
            x = (emp[0],emp[1],minimax(newboard,depth-1,'MAX',K)[2])
            if bestValue[2]>x[2]:
                bestValue=x
        return bestValue
    raise 
    
def postaw(board, kk, k, player):
    global DEPTH
    #według algorytmu minimax
    #stawia kk na board wg nie losowego algorytmu,
    for emp in empty(board):
        win,sign  = czywygrana(put(board,kk,emp),k)
        if sign=='o' or sign=='x': 
            return emp
    if DEPTH==-1:
        DEPTH=ceil(len(empty(board))/2)
    if DEPTH>len(empty(board)):
        DEPTH=len(empty(board))
    if DEPTH==-2:
        DEPTH=len(empty(board))
    y = minimax(board,DEPTH,player,k)[:2]
    return y
        

def czywygrana(board,k):
    ## funkcja do sprawdzania czy dana plansza jest końcowa
    ## funkcja nagrody
    win = re.compile('(x{'+str(k)+'}|o{'+str(k)+'})')
    xpos,ypos=board[-1]
    size = len(board[0])
    #wiersz
    winner = win.search(board[xpos])
    if winner:
        return True, winner.group(0)[0]
    #kolumna
    tmp = ''.join([board[x][ypos] for x in range(size-ypos)])
    winner = win.search(tmp)
    if winner:
        return True, winner.group(0)[0]
    #\
    if xpos>ypos:
        tmp =''.join([board[xpos-ypos+x][x] for x in range(ceil((size-xpos+ypos)/2))])
    else:
        tmp =''.join([board[x][ypos-xpos+x] for x in range(ceil((size-ypos+xpos)/2))])
    winner = win.search(tmp)
    if winner:
        return True, winner.group(0)[0]
    #/
    tmp=''.join([board[xpos+ypos-x][x] for x in range(xpos+ypos+1)])
    winner = win.search(tmp)
    if winner:
        return True, winner.group(0)[0]
    if not empty(board):
        return True,'Remis'
    return False,''

def puto(board, K):
    return put(board,'o',postaw(board,'o',K,'MIX'))
    

def putx(board, K):
    return put(board,'x',postaw(board,'o',K,'MAX'))

def controlled_o(board, K):
    while True:
        try:
            x = int(input('Wiersz: '))
            y = int(input('Kolumna: '))
            if (x,y) not in empty(board):
                raise
        except:
            print('Podana wartość jest nieprawidłowa')
            continue
        break
    return put(board,'o',(x,y))

def rozgrywka(postawkolko, postawkrzyzyk, N, K):
    global VALUES
    board = genBoard(N)
    drawBoard(board)
    move_o= True
    st = time.time()
    while True:
        if move_o:
            board = postawkolko(board,K)
            move_o=False
        else:
            board = postawkrzyzyk(board,K)
            move_o=True
        drawBoard(board)
        if verb: print(time.time()-st)
        win, sign = czywygrana(board,K)
        if win:
            if len(sign)==1:
                print('Wygrał {}'.format(sign))
            else:
                print(sign)
            break
def main():
    size = args.size
    k = args.line
    st = time.time()
    if not args.controlled:
        rozgrywka(controlled_o, putx, size, k)
    else:
        rozgrywka(puto, putx, size,k)
    if verb: print(time.time()-st)
    
if __name__ == "__main__":
    main()

## why is this here??????????
plansza = genBoard(5)
k = 3
