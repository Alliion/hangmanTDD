import random
import unittest

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'mistake', 'vegas', 'liberty', 'depth',
    'guide', 'agreement', 'tosha', 'alina'
]

class Hangman():

    def __init__(self, word_to_guess):


    def find_indexes(self, letter):


    def is_invalid_letter(self, input_):


class GameProcess():

    def update_progress(self, letter, indexes):


    def get_user_input(self):


class Play(Hangman, GameProcess):

    def play(self):


if __name__ == '__main__':
    word_to_guess = random.choise(WORDS)
    hangman = Play(word_to_guess)
    hangman.play()

class Tests(unittest.TestCase):

    def find_indexes_test(self):
        self.assertTrue(self, 0, 0)
