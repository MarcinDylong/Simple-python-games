from unittest import TestCase

from logic import isWinner, isBoardFilled

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertFalse(False)


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