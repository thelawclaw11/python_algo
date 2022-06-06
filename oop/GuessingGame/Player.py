import random


class Picker:
    def __init__(self):
        self.number = None

    def pick_number(self):
        self.number = random.randint(1, 10)

    def is_guess_correct(self, guess: int):
        if guess != self.number:
            print("PLAYER: guess is not correct!")

        return guess == self.number

    def lose(self):
        print(F"PICKER: You guessed my number! It was {self.number}!")

    def win(self):
        print(F"PICKER: You didn't guess my number! It was {self.number}!")







