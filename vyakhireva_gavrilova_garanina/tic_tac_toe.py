import random

b = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def board(b):
    print(b[0], '|', b[1], '|', b[2])
    print('--+---+--')
    print(b[3], '|', b[4], '|', b[5])
    print('--+---+--')
    print(b[6], '|', b[7], '|', b[8])
    
coin = ['heads', 'tails']
toss1 = random.choice(coin)
toss2 = input("Welcome to Tic-tac-toe game!\nLet's toss to see who'll go first, you or computer... Heads or tails? ")

if toss1 == toss2.lower():
    print("It's {}! You go first!".format(toss1))
    board(b)
    us = int(input('Choose a number on the board to place a cross (X) ')) #us - user
    b[us] = 'X'
    board(b)
    
elif toss1 != toss2.lower():
    print("It's {}. Computer goes first.".format(toss1))
    b[0] = 'X'
    board(b)
    us = int(input('Choose a number on the board to place a nought (O) '))
    b[us] = 'O'

    def win(x2, o2, x3, o3_1, o3_2, o3_3, x4_1, x4_2):
        b[x2] = 'X'
        board(b)
        us = int(input('Choose a number on the board to place a nought (O) '))
        b[us] = 'O'
        if b[o2] == 'O':
            b[x3] = 'X'
            board(b)
            us = int(input('Choose a number on the board to place a nought (O) '))
            b[us] = 'O'
            if b[o3_1] == 'O' or b[o3_2] == 'O' or b[o3_3] == 'O':
                b[x4_1] = 'X'
                board(b)
            elif b[x4_1] == 'O':
                b[x4_2] = 'X'
                board(b)
        else:
            b[o2] = 'X'
            board(b)
        print('Computer won.')
            
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

    '''elif b[4] == 'O':'''

    


        
    
        
        
