from unittest import TestCase

from logic import  insertLetterToBoard, isWinner, isBoardFilled, \
    createEmptyBoard, determineComputerMove

class testInsertLetterToBoard(TestCase):
    """ IndexError will be handle in playerMove()"""
    def setUp(self):
        self.board = createEmptyBoard()

    def testInsertLetter1(self):
        insertLetterToBoard(self.board, 'X', 2)
        self.assertEqual(self.board[2], 'X')

    def testInsertLetter1(self):
        insertLetterToBoard(self.board, 'c', 9)
        self.assertEqual(self.board[9], 'c')


class testIsWinner(TestCase):
    def setUp(self):
        self.X = 'X'
        self.O = 'O' 

    def testsIsWinner1(self):
        board = [' ', 'X', 'X', 'X', ' ', 'O', 'O', 'X', 'X', ' ']
        self.assertTrue(isWinner(board, self.X), 'Should return True')

    def testsIsWinner2(self):
        board = [' ', 'X', 'X', 'X', ' ', 'O', 'O', 'X', 'X', ' ']
        self.assertFalse(isWinner(board, self.O), 'Should return False')

    def testsIsWinner3(self):
        board = [' ', 'X', ' ', 'X', ' ', 'X', 'O', 'X', 'O', 'O']
        self.assertTrue(isWinner(board, self.X), 'Should return True')

    def testsIsWinner4(self):
        board = [' ', 'X', 'O', 'X', ' ', 'O', 'O', 'X', 'X', ' ']
        self.assertFalse(isWinner(board, self.X), 'Should return False')

    def testsIsWinner5(self):
        board = [' ', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', ' ']
        self.assertTrue(isWinner(board, self.O), 'Should return True')


class testIsBoardFilled(TestCase):
    def testIsBoardFilled1(self):
        board = [' ', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', ' ']
        self.assertFalse(isBoardFilled(board),'Should return False')

    def testIsBoardFilled2(self):
        board = [' ', 'X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', 'O']
        self.assertTrue(isBoardFilled(board), 'Should return True')

    def testIsBoardFilled3(self):
        board = [' ', 'X', 'O', ' ', 'O', ' ', 'O', 'X', 'X', ' ']
        self.assertFalse(isBoardFilled(board), 'Should return False')


class testDetermineComputerMove(TestCase):
    def testComputerMove1(self):
        board = [ ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ',
            ]
        move = determineComputerMove(board)
        self.assertEqual(5,move)

    def testComputerMove2(self):
        board = [ ' ',
            'X', ' ', ' ',
            ' ', 'X', ' ',
            ' ', ' ', ' ',
            ]
        move = determineComputerMove(board)
        self.assertEqual(9,move)

    def testComputerMove3(self):
        board = [ ' ',
            'X', ' ', 'O',
            'X', ' ', 'O',
            ' ', ' ', ' ',
            ]
        move = determineComputerMove(board)
        self.assertEqual(9,move)