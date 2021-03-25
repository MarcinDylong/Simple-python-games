from tic_tac_toe import playerMove, computerMove, createEmptyBoard, isWinner,\
    displayBoard, isBoardFilled
from hangman import Progress

def choose_game():
    print('[1] - Tic tac toe')
    print('[2] - Hangman')
    print('[0] - Exit')
    choice = input('Write your choice!  ')
    try:
        if int(choice) >= 0 and int(choice) <= 2:
            return int(choice)
        else:
            print('Your choice is out of range!')
            return None
    except ValueError:
        print('Invalid input!')
        return None
    

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

    
    while True:
        print('WELCOME!!')
        print('Choose the game you want to play!')
        choice = choose_game()

        if choice == 0:
            print('########\nGoodbye!\n########')
            break
        elif choice == 1:    
            ## Play tic tac toe
            print('Welcome to Tic Tac Toe!')
            print('To win, you have to complete straight line of three \'X\'')
            print('The board has grid numbered from 1-9')
            while True:
                tic_tac_toe()
                again = input('Would like to play again? (y/n)')

                if again.lower() == 'n' or again.lower() == 'no':
                    print('########\nYou are leaving tic tac toe\n########')
                    break 
        elif choice == 2:
            ## Play hangman
            print('Welcome to Hangman!')
            print('Guess the word before you before you get hanged!')
            while True:
                hangman()
                again = input('Would like to play again? (y/n)')

                if again.lower() == 'n' or again.lower() == 'no':
                    print('########\nYou are leaving hangman!\n########')
                    break 
        else:
            continue
            