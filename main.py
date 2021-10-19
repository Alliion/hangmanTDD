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


class Hangman:

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = list('_' * len(self.word_to_guess))

    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]

    def is_invalid_letter(self, input_):
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)


def get_user_input():
    user_input = input('\nPlease type a letter: ')
    return user_input


class GameProcess(Hangman):

    def print_game_status(self):
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index] = letter


class Play(GameProcess):

    def play(self):
        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('¡The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.word_to_guess))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n¡OMG! You lost!")


if __name__ == '__main__':
    word_to_guess = random.choice(WORDS)
    hangman = Play(word_to_guess)
    hangman.play()


class Tests(unittest.TestCase):

    def find_indexes_test(self):
        self.assertTrue(self, 0, 0)
