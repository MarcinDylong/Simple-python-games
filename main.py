from logic import playerMove, computerMove, createEmptyBoard, displayBoard,\
    isWinner, isBoardFilled

def game():
    ## Game start
    

    board = createEmptyBoard()
    displayBoard(board)
    ## loop for simple game
    while True:
        if not(isWinner(board, 'O')):
            playerMove(board)
            displayBoard(board)
        else:
            print('Computer won ;(')
            break

        if isBoardFilled(board):
            print('Tie! Board is full!')
            break

        if not(isWinner(board, 'X')):
            computerMove(board)
            displayBoard(board)
        else:
            print('You won :)!')
            break
        print('\n###########\n')


if __name__ == '__main__':
    ## Greetings
    print('Welcome to Tic Tac Toe!')
    print('To win, you have to complete straight line of three \'X\'')
    print('The board has grid numbered from 1-9')
    while True:
        game()
        again = input('Would like to play again? (y/n)')

        if again.lower() == 'n' or again.lower() == 'no':
            print('########\nGoodbye!\n########')
            break 
