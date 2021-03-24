def createEmptyBoard():
    """Create empty list which represents board"""
    board = [' ' for i in range(10)]
    return board

def insertLetterToBoard(let, pos, board):
    board[pos] = let

def isGridEmpty(pos):
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
    empties = [True for b in board if b == ' ']
    return len(empties) == 1

def playerMove():
    while True:
        move = input('Choose grid from (1-9) to insert X: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isGridEmpty(move):
                    insertLetterToBoard('X', move)
                    break
                else:
                    print('Grid is already taken!')
            else:
                print('Move outside the range, choose between 1-9')
        except ValueError:
            print('Invalid input')

if __name__ == '__main__':
    pass