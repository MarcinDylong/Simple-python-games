import io
import unittest.mock
from unittest import TestCase


from hangman import Progress


class TestDisplayWord(TestCase):
    def setUp(self):
        self.progress = Progress()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testDisplayWord1(self, mock_stdout):
        self.progress.word = 'BANANA'
        self.progress.used_letters = ['B','A', 'M']
        self.progress.displayWord()
        self.assertEqual(mock_stdout.getvalue(), 'B A _ A _ A\n')
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testDisplayWord2(self, mock_stdout):
        self.progress.word = 'PINEAPPLE'
        self.progress.used_letters = ['P','E', 'R', 'M']
        self.progress.displayWord()
        self.assertEqual(mock_stdout.getvalue(), 'P _ _ E _ P P _ E\n')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def testDisplayWord3(self, mock_stdout):
        self.progress.word = 'LEMON'
        self.progress.used_letters = ['C','U', 'S']
        self.progress.displayWord()
        self.assertEqual(mock_stdout.getvalue(), '_ _ _ _ _\n')

    def testProgressBar1(self):
        self.assertEqual(
            self.progress._progress_bar,
            [' ',' ',' ',' ',' ',' ']
            )

    def testProgressBar2(self):
        self.progress._update_progress_bar()
        self.assertEqual(
            self.progress._progress_bar,
            ['o',' ',' ',' ',' ',' ']
            )

    def testProgressBar3(self):
        self.progress._update_progress_bar()
        self.progress._chances = 5
        self.progress._update_progress_bar()
        self.assertEqual(
            self.progress._progress_bar, 
            ['o','|',' ',' ',' ',' ']
            )

    def testIsOver1(self):
        self.progress.used_letters = ['C', 'B', 'A']
        self.progress.word_letters = ['B', 'C', 'A']
        self.assertEqual(
            self.progress.is_over(),
            True
        )

    def testIsOver2(self):
        self.progress._chances = 0
        self.assertEqual(
            self.progress.is_over(),
            True
        )

    def testIsOver3(self):
        self.progress.used_letters = ['C', 'B', 'A', 'D']
        self.progress.word_letters = ['B', 'C', 'A']
        self.assertEqual(
            self.progress.is_over(),
            True
        )

    def testIsOver4(self):
        self.progress._chances = 2
        self.assertEqual(
            self.progress.is_over(),
            False
        )