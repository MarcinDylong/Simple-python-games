from unittest import TestCase

from sudoku import find_first_empty, is_empty, is_valid, solve_board


class testFindFirstEmpty(TestCase):
    def testReturnElemR0C0(self):
        board = [
            [0,0,9,0,7,0,0,4,0],
            [4,0,3,0,0,2,6,0,7],
            [0,6,0,0,0,0,9,3,1],
            [6,1,0,5,0,8,0,0,0],
            [0,2,0,4,0,0,0,0,0],
            [8,0,5,0,0,0,0,0,6],
            [9,0,0,6,0,0,5,8,2],
            [0,0,0,2,0,0,7,9,0],
            [2,3,0,7,0,5,0,0,4]
        ]
        self.assertEqual(find_first_empty(board), (0,0))


    def testReturnElemR1C1(self):
        board = [
            [1,2,9,3,7,5,6,4,8],
            [4,0,3,0,0,2,6,0,7],
            [0,6,0,0,0,0,9,3,1],
            [6,1,0,5,0,8,0,0,0],
            [0,2,0,4,0,0,0,0,0],
            [8,0,5,0,0,0,0,0,6],
            [9,0,0,6,0,0,5,8,2],
            [0,0,0,2,0,0,7,9,0],
            [2,3,0,7,0,5,0,0,4]
        ]
        self.assertEqual(find_first_empty(board), (1,1))

    def testdReturnNone(self):
        board = [
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8],
            [1,2,9,3,7,5,6,4,8]
        ]
        self.assertEqual(find_first_empty(board), None)


class testIsEmptyIsValidSolveBoard(TestCase):
    def setUp(self):
        self.board = [
            [4,3,0,0,0,0,2,9,7],
            [6,8,0,0,7,2,0,0,0],
            [2,0,0,0,0,4,5,0,0],
            [0,0,3,0,5,8,4,0,0],
            [1,0,0,0,4,0,0,5,9],
            [0,5,0,0,0,0,0,0,0],
            [0,0,2,0,0,1,0,0,0],
            [8,0,6,7,0,3,0,0,0],
            [0,7,9,0,0,5,0,8,0]
        ]

    def testIsEmptyReturnTrue(self):
        self.assertEqual(
            is_empty(self.board, (0,0)), False
        )

    def testIsEmptyReturnFalse(self):
        self.assertEqual(
            is_empty(self.board, (2,2)), True
        )

    def testIsValidReturnTrue(self):
        self.assertEqual(
            is_valid(self.board,5,(6,0)), True
        )

    def testIsValidReturnFalse(self):
        self.assertEqual(
            is_valid(self.board,6,(6,0)), False
        )

    def testSolveBoardTrue(self):
        self.assertEqual(
            solve_board(self.board), True
        )

    def testSolveBoardFalse(self):
        self.board[0][0] = 3
        self.assertEqual(
            solve_board(self.board), False
        )