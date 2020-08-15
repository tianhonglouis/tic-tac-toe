# -*- coding:utf8 -*-
import random

def print_blackboard(board):
    for i in range(7):
        if i%2 == 0:
            print '+'.join(['---']*3)
        else:
            col = []
            for j in range(11):
                if j%2 == 0:
                    col.append(' ')
                elif j==3 or j==7:
                    col.append('|')
                else:
                    col.append(board[i/2][j/4])
            print ''.join(col)

def get_the_one_go():
    if random.randint(0, 1):
        return 'AI'
    else:
        return 'P'

def play_again():
    print "Once Again?(y for Yes, n for No)"
    return raw_input().lower().startswith('y')

def next(board, letter, move):
    seq = move-1
    board[2-seq/3][seq%3] = letter

def iswin(bo, le):
    return ((bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or
    (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or
    (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or
    (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or
    (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or
    (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or
    (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or
    (bo[0][2] == le and bo[1][1] == le and bo[2][0] == le))

def copy_blackboard(board):
    duplicate = [[' ']*3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            duplicate[i][j] = board[i][j]
    return duplicate

def is_space_have(board, move):
    seq = move-1
    return board[2-seq/3][seq%3] == ' '

def get_P_moves(board):
    move = ''
    while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_space_have(board, move):
        print "Please input your next move('1-9')"
        move = input()
    return move

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def choose_randomly(board, avail):
    possible_moves = []
    for i in avail:
        if is_space_have(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def get_computer_moves(board, AI, P):
    for i in range(1, 10):
        copy = copy_blackboard(board)
        if is_space_have(board, i):
            next(copy, AI, i)
            if iswin(copy, AI):
                return i

    for i in range(1, 10):
        copy = copy_blackboard(board)
        if is_space_have(board, i):
            next(copy, P, i)
            if iswin(copy, P):
                return i

    move = choose_randomly(board, [1, 3, 7, 9])
    print move
    if move != None:
        return move

    if is_space_have(board, 5):
        return 5

    return choose_randomly(board, [2, 4, 6, 8])

if __name__ == '__main__':

    while True:
        Board = [[' ']*3 for i in range(3)]
        P, COMPUTER = 'x', 'o'
        turn = get_the_one_go()
        print "{0} will go first".format(turn)
        GameOn = True

        while GameOn:
            if turn == 'P':
                move = get_P_moves(Board)
                next(Board, P, move)
                print_blackboard(Board)

                if iswin(Board, P):
                    print_blackboard(Board)
                    print "GameOver You've Won!"
                    GameOn = False
                else:
                    if is_board_full(Board):
                        print_blackboard(Board)
                        print "Tie"
                        break
                    else:
                        turn = 'AI'

            else:
                move = get_computer_moves(Board, COMPUTER, P)
                next(Board, COMPUTER, move)
                print_blackboard(Board)

                if iswin(Board, COMPUTER):
                    print_blackboard(Board)
                    print "GameOver Computer has Won!"
                    GameOn = False
                else:
                    if is_board_full(Board):
                        print_blackboard(Board)
                        print "Tie"
                        break
                    else:
                        turn = 'P'

        if not play_again():
            break
