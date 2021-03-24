from random import shuffle

def createEmptyBoard():
    """Create empty list which represents board"""
    board = [' ' for i in range(10)]
    return board

def insertLetterToBoard(board, letter, pos):
    board[pos] = letter

def isGridEmpty(board, pos):
    return True if board[pos] == ' ' else False

def displayBoard(board):
    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('   |   |   ')


def isWinner(board, letter):
    letter_pos = set([i for i in range(len(board)) if board[i]==letter])
    wining_combinations = [
        {1,2,3}, {4,5,6}, {7,8,9},
        {1,4,7}, {2,5,8}, {3,6,9},
        {1,5,9}, {3,5,7}
    ]
    for w in wining_combinations:
        if w <= letter_pos:
            return True
    return False


def isBoardFilled(board):
    if len([True for b in board if b == ' ']) == 1:
        return True
    else:
        return False


def playerMove(board):
    while True:
        move = input('Choose grid from (1-9) to insert X: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isGridEmpty(board, move):
                    insertLetterToBoard(board, 'X', move)
                    break
                else:
                    print('Grid is already taken!')
            else:
                print('Move outside the range, choose between 1-9')
        except ValueError:
            print('Invalid input')


def determineComputerMove(board):
    emptyGrids = [i for i in range(1,len(board)) if board[i] == ' ']

    ## Check Winning move
    for grid in emptyGrids:
        temp_board = board.copy()
        insertLetterToBoard(temp_board, 'O', grid)
        if isWinner(temp_board, 'O'):
            return grid

    ## Check player winning move
    for grid in emptyGrids:
        temp_board = board.copy()
        insertLetterToBoard(temp_board, 'X', grid)
        if isWinner(temp_board, 'X'):
            return grid

    ## Take Center if available
    if isGridEmpty(board, 5):
        return 5

    ## Take corner else take last element from shuffled list
    shuffle(emptyGrids)
    for grid in emptyGrids:
        if grid in [1,3,7,9]:
            return grid
    
    return emptyGrids[0]
    

def computerMove(board):
    move = determineComputerMove(board)
    print(f'\nComputer played on position {move}')
    insertLetterToBoard(board, 'O', move)


if __name__ == '__main__':
    pass