import copy

from boards import sudoku_boards
from random import choice



def random_board():
    return choice(sudoku_boards)


def print_board(board):
    print('   | 1 2 3    4 5 6    7 8 9')
    print('---|-----------------------')
    for i in range(len(board)):
        ## Separate squares horizontally
        if i % 3 == 0 and i != 0:
            print('   | - - - - - - - - - - - -')
        print(f' {i+1} | ', end="")
        for j in range(len(board[0])):
            ## Separate squares vertically
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')


def find_first_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    ## If no empty cell found
    return None


def is_empty(board, pos):
    r,c = pos
    if board[r][c] == 0:
        return True
    else:
        return False


def is_valid(board, number, pos):
    ## Coordinates
    r,c = pos
    ## Row
    for i in range(len(board[0])):
        ## Exact cell
        if i == c:
            continue
        if board[r][i] == number:
            return False        
    ## Column
    for i in range(len(board)):
        ## Exact cell
        if i == r:
            continue

        if board[i][c] == number:
            return False
    ## Square
    # Determine row and column for square ()
    rs, cs = r//3, c//3
    for i in range(3):
        for j in range(3):
            if (i+3*rs, j+3*cs) == pos:
                continue
            if board[i+3*rs][j+3*cs] == number:
                return False
    return True


def solve_board(board):
    empty = find_first_empty(board)
    if not empty:
        return True
    else: 
        r, c = empty
    for i in range(1,10):
        if is_valid(board, i, (r,c)):
            board[r][c] = i
            if solve_board(board):
                return True
            board[r][c] = 0
    ## In case if unsolvable
    return False


def check_user_input(inp):
    try:
        inp = int(inp)
        if inp > 0 and inp <10:
            return True 
        else:
            print('Input should be number between 1-9')
            return False
    except ValueError:
        print('Input should be number between 1-9')
        return False


def user_input(board):
    while True:
        r = input('Insert row number from 1-9: ')
        if check_user_input(r):
            break
    while True:
        c = input('Insert column number from 1-9: ')
        if check_user_input(c):
            break
    while True:
        number = input('Insert column number from 1-9: ')
        if check_user_input(number):
            break
    r, c, number = int(r)-1, int(c)-1, int(number)
    return r,c,number

def insert_num(board, r, c, number):
    temp = copy.deepcopy(board)
    ## Check if cell is empty
    if is_empty(temp, (r,c)):
        temp[r][c] = number
        ## Try to solve sudoku with given number in cell
        if solve_board(temp):
            board[r][c] = number
            print(f'\n{number} is correct!\n')
            return True
        else:
            print(f'\n{number} is not valid for row {r+1} and column {c+1}\n')
            return False
    else:
        print(f'\nRow {r+1}, column {c+1} is already occupied!\n')
        return False
    


if __name__ == '__main__':
    pass