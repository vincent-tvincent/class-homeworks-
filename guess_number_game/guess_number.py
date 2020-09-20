import random


class guess_number:

    def guess_number(self):
        number = int(input("what's your guess?: "))
        print("guess number: " + str(number))
        return number

    def random_guess_number(self, minimum, maximum):
        number = random.randint(minimum, maximum)
        print("guess number: " + str(number))
        return number

