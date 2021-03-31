ex_board = [
    [0,0,9,0,7,0,0,4,0],
    [4,0,3,0,0,2,6,0,7],
    [0,6,0,0,0,0,9,3,1],
    [6,1,0,5,0,8,0,0,0],
    [0,2,0,4,0,0,0,0,0],
    [8,0,5,0,0,0,0,0,6],
    [9,0,0,6,0,0,5,8,2],
    [0,0,0,2,0,0,7,9,0],
    [2,3,0,7,0,5,0,0,4],
]


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
                return i,j
    ## If no empty cell found
    return None


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

    

if __name__ == '__main__':
    print_board(ex_board)
    # print('---------------')
    # solve_board(ex_board)
    # print_board(ex_board)