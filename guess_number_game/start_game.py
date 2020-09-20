from guess_number import guess_number
import random


class start_game(guess_number):
    __max_range = 0
    __min_range = 0
    __target = 0

    def __init__(self, target):
        self.__target = target
        self.__max_range = random.randint(target, target + 10)
        self.__min_range = random.randint(target - 10, target)

    def get_data(self):
        print("max: " + str(self.__max_range))
        print("min: " + str(self.__min_range))
        print("target: " + str(self.__target))
    def get_min(self):
        return self.__min_range
    def get_max(self):
        return self.__max_range

    def player_guess(self, guess_time=1):
        print("the range is between " + str(self.__max_range) + " and " + str(self.__min_range))
        guess = super().guess_number()
        if guess == self.__target:
            print("correct answer, you tried " + str(guess_time) + " times. ")
            return
        elif guess < self.__target:
            print("too small, try again")
            self.player_guess(guess_time + 1)
        elif guess > self.__target:
            print("too big, try again")
            self.player_guess(guess_time + 1)

    def computer_guess(self, guess_time=1, min = None, max = None):
        guess_min = self.__min_range
        guess_max = self.__max_range

        if min != None:
            guess_min = min
        if max != None:
            guess_max = max
        guess = super().random_guess_number(guess_min, guess_max)

        if guess == self.__target:
            print("correct answer, computer tried " + str(guess_time) + " times. ")
            return
        elif guess < self.__target:
            print("too small, try again")
            self.computer_guess(guess_time + 1, min=guess + 1, max=guess_max)
        elif guess > self.__target:
            print("too big, try again")
            self.computer_guess(guess_time + 1, min=guess_min, max=guess - 1)
