from oop.GuessingGame.Guesser import Guesser
from oop.GuessingGame.Player import Picker


class Game:
    def __init__(self, guesses):
        self.picker = Picker()
        self.guesser = Guesser()
        self.guesses_remaining = guesses

    def play_game(self):
        print("GAME: game starting...")
        self.picker.pick_number()

        while True:
            if self.guesses_remaining == 0:
                return self.end_game(True)

            current_guess = self.guesser.guess()
            is_correct = self.picker.is_guess_correct(current_guess)

            if is_correct:
                return self.end_game(False)

            self.guesses_remaining -= 1

    def end_game(self, player_wins):
        if player_wins:
            self.picker.win()
            self.guesser.lose()
        else:
            self.picker.lose()
            self.guesser.win()
        print("GAME: game complete")