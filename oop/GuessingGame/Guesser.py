import random


class Guesser:
    def __init__(self):
        self.available_guesses = set(range(1,11))

    def guess(self):
        guess = random.choice(list(self.available_guesses))
        self.available_guesses.remove(guess)
        print(f"GUESSER: I guess {guess}")
        return guess

    @staticmethod
    def win():
        print("GUESSER: I guessed your number!")

    @staticmethod
    def lose():
        print("GUESSER: I Lose")

