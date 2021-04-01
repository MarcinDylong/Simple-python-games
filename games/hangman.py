from random import randint
from string import ascii_letters

class Progress:

    word_bank = [
    'BANANA', 'JAVA-PLUM', 'JACKFRUIT', 'KUMQUAT', 'MULBERRIES', 'NECTARINE',
    'PINEAPPLE', 'LYCHEE', 'MANGOSTEEN', 'PITAYA', 'PERSIMMON', 'POMEGRANATE',
    'APPLE', 'PUMMELO', 'QUINCE', 'RASPBERRIES', 'TANGERINE', 'WATERMELON',
    'HONEYDEW MELON', 'AVOCADO', 'COCONUT MEAT', 'ELDERBERRIES', 'GUAVA'
    ]
    
    def __init__(self):
        random = randint(0, len(Progress.word_bank)-1)
        self.word = Progress.word_bank[random]
        word_letters = list(set([w for w in self.word if w not in ['-', ' ']]))
        self.word_letters = word_letters
        self.used_letters = []
        self._chances = 6
        self._progress_bar = [' ' for i in range(6)]

    def _update_progress_bar(self):
        signs = ['o', '|', '/', '\\', '/', '\\']
        self._progress_bar[6 - self._chances] = signs[6 - self._chances]

    def _add_letter(self, letter):
        self.used_letters.append(letter)

    def check_user_letter(self, letter):
        if letter in self.used_letters:
            print(f'{letter} is already used!')
        elif letter in self.word_letters:
            self.used_letters.append(letter)
            print(f'{letter} is present in a word!')
        else:
            self.used_letters.append(letter)
            self._update_progress_bar()
            self._chances -= 1
            print(f'{letter} is not present in a word!')

    def is_over(self):
        if set(self.used_letters) >= set(self.word_letters):
            print(f'\n{self.word}\nGreat, You guessed!\n')
            return True
        elif self._chances == 0:
            print('You hung up! ;(')
            self.displayHangman()
            print(f'The word was {self.word}')
            return True
        else:
            return False

    def displayHangman(self):
        bar = self._progress_bar
        print(' ______')
        print(' |/   |')
        print(f' |    {bar[0]}')
        print(f' |   {bar[2]}{bar[1]}{bar[3]}')
        print(f' |   {bar[4]} {bar[5]}')
        print(' |')
        print(' |')
        print('_|_')

    def displayWord(self):
        word = self.word
        used_letters = self.used_letters
        display = []
        for w in word:
            if w in used_letters:
                display.append(w)
            elif w in [' ', '-']:
                display.append(' ')
            else:
                display.append('_') 
        print(' '.join(display))

    def displayUsedLetters(self):
        print(f'\nLetter already used: {" ".join(self.used_letters)}')

    def userInput(self):
        while True:
            letter = input('\nPick the letter! ')
            if letter in ascii_letters:
                self.check_user_letter(letter.upper())
                break
            else:
                print('Invalid input!')

if __name__ == '__main__':
    pass