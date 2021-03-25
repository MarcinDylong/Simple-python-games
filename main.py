from tic_tac_toe import playerMove, computerMove, createEmptyBoard, isWinner,\
    displayBoard, isBoardFilled
from hangman import Progress

def tic_tac_toe():
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


def hangman():
    ## Game start
    progress = Progress()
    ## loop for simple game
    while True:
        progress.displayHangman()
        print('Word to guess:\n')
        progress.displayWord()
        progress.displayUsedLetters()
        progress.userInput()
        if progress.is_over():
            break



if __name__ == '__main__':
    # ## Greetings
    # print('Welcome to Tic Tac Toe!')
    # print('To win, you have to complete straight line of three \'X\'')
    # print('The board has grid numbered from 1-9')
    # while True:
    #     tic_tac_toe()
    #     again = input('Would like to play again? (y/n)')

    #     if again.lower() == 'n' or again.lower() == 'no':
    #         print('########\nGoodbye!\n########')
    #         break 

    ## Greetings
    print('Welcome to Hangman!')
    print('Guess the word before you before you get hanged!')
    while True:
        hangman()
        again = input('Would like to play again? (y/n)')

        if again.lower() == 'n' or again.lower() == 'no':
            print('########\nGoodbye!\n########')
            break 