import random

user = 0
computer = 0
roundd = 'yes'

def board(b):
    print('\n'+ str(b[0]), '|', b[1], '|', b[2])
    print('--+---+--')
    print(b[3], '|', b[4], '|', b[5])
    print('--+---+--')
    print(b[6], '|', b[7], '|', b[8])

def win(x2, o2, x3, o3_1, o3_2, o3_3, x4_1, x4_2):
    b[x2] = 'X'
    board(b)
    global us
    while us not in b:
        us = int(input('\nChoose a number on the board to place a nought (O) '))
    b[us] = 'O'
    if b[o2] == 'O':
        b[x3] = 'X'
        board(b)
        while us not in b:
            us = int(input('\nChoose a number on the board to place a nought (O) '))
        b[us] = 'O'
        if b[o3_1] == 'O' or b[o3_2] == 'O' or b[o3_3] == 'O':
            b[x4_1] = 'X'
        elif b[x4_1] == 'O':
            b[x4_2] = 'X'
    else:
        b[o2] = 'X'
    board(b)
    global computer
    computer += 1
    print('\nComputer won.')

def win_symmetry(x3, o3_1, o3_2, o3_3, x4_1, x4_2):
    b[x3] = 'X'
    board(b)
    global us
    while us not in b:
        us = int(input('\nChoose a number on the board to place a nought (O) '))
    b[us] = 'O'
    if b[o3_1] == 'O' or b[o3_2] == 'O' or b[o3_3] == 'O':
        b[x4_1] = 'X'
    elif b[x4_1] == 'O':
        b[x4_2] = 'X'
    board(b)
    global computer
    computer += 1
    print('\nComputer won.')

def cats_game(x3, o3, x4, o4, x5):
    b[x3] = 'X'
    board(b)
    global us
    while us not in b:
        us = int(input('\nChoose a number on the board to place a nought (O) '))
    b[us] = 'O'
    if b[o3] == 'O':
        b[x4] = 'X'
        board(b)
        while us not in b:
            us = int(input('\nChoose a number on the board to place a nought (O) '))
        b[us] = 'O'
        if b[o4] == 'O':
            b[x5] = 'X'
            board(b)
            print ("\nIt's a cat! meow :)")
        else:
            b[o4] = 'X'
            board(b)
            global computer
            computer += 1
            print('\nComputer won.')  
    else:
        b[o3] = 'X'
        board(b)
        computer += 1
        print('\nComputer won.')

def usgf(l): #user goes first
    if len(l) - len(set(l)) == 2:
        if all(i == 'X' for i in l):
            global user
            user += 1
            print('You won!')
        elif all(i == 'O' for i in l):
            global computer
            conputer += 1
            print('Computer won.')
        global win
        win = 1
    
print('Welcome to Tic-tac-toe game!')

while roundd == 'yes':
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    coin = ['heads', 'tails']
    toss1 = random.choice(coin)
    toss2 = input("\nLet's toss to see who'll go first, you or computer... Heads or tails? ")
    
    if toss1 == toss2.lower():
        print("\nIt's {}! You go first!".format(toss1))
        while not all(isinstance(i, str) for i in b):
            board(b)
            us = 9
            while us not in b:
                us = int(input('\nChoose a number on the board to place a cross (X) ')) #us - user
            b[us] = 'X'
            nought = 0
            win = 0
            usgf([b[0], b[1], b[2]])
            usgf([b[2], b[5], b[8]])
            usgf([b[6], b[7], b[8]])
            usgf([b[0], b[3], b[6]])
            usgf([b[1], b[4], b[7]])
            usgf([b[3], b[4], b[5]])
            usgf([b[0], b[4], b[8]])
            usgf([b[2], b[4], b[6]])
            if win == 1:
                break
            else:
                l = []
                for i in b:
                    if isinstance(i, int):
                        l.append(i)
                o_n = random.choice(l)
                b[o_n] = 'O'
        else:
            print("\nIt's a cat! meow :)")
                
    elif toss1 != toss2.lower():
        print("\nIt's {}. Computer goes first.".format(toss1))
        b[0] = 'X'
        board(b)
        us = 0
        while us not in b:
            us = int(input('\nChoose a number on the board to place a nought (O) '))
        b[us] = 'O'
        
        if b[1] == 'O':
            win(6, 3, 4, 2, 5, 7, 8, 2)
        elif b[2] == 'O':
            win(8, 4, 6, 1, 3, 5, 7, 3)
        elif b[3] == 'O':
            win(2, 1, 8, 5, 6, 7, 4, 5)
        elif b[5] == 'O':
            win(2, 1, 6, 3, 7, 8, 4, 3)
        elif b[6] == 'O':
            win(2, 1, 8, 3, 5, 7, 4, 5)
        elif b[7] == 'O':
            win(2, 1, 4, 3, 5, 6, 8, 6)
        elif b[8] == 'O':
            win(6, 3, 2, 1, 5, 7, 4, 1)
            
        elif b[4] == 'O':
            b[8] = 'X'
            board(b)
            while us not in b:
                us = int(input('\nChoose a number on the board to place a nought (O) '))
            b[us] = 'O'
            if b[2] == 'O':
                win_symmetry(6, 1, 3, 5, 7, 3)
            elif b[6] == 'O':
                win_symmetry(2, 3, 5, 7, 1, 5)
            elif b[1] == 'O':
                cats_game(7, 6, 2, 5, 3)
            elif b[3] == 'O':
                cats_game(5, 2, 6, 7, 1)
            elif b[5] == 'O':
                cats_game(3, 6, 2, 1, 7)
            elif b[7] == 'O':
                cats_game(1, 2, 6, 3, 5)

    print('\nHere is the score. You {}:{} Computer'.format(user, computer))
    roundd = input('\nWanna play again? yes/no ').lower()

        

    


        
    
        
        
