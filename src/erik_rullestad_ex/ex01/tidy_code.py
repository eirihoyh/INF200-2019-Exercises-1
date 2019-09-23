from random import randint

__author__ = 'Erik Rullestad'
__email__ = 'erikrull@nmbu.no'


def guess_number():
    my_guess = 0
    while my_guess < 1:
        my_guess = int(input('Your guess: '))
    return my_guess


def sum_of_two_dices():
    return randint(1, 6) + randint(1, 6)


def equal_variables(variable1, variable2):
    return variable1 == variable2


if __name__ == '__main__':

    boolean_value = False
    number_of_tries = 3
    number = sum_of_two_dices()
    while not boolean_value and number_of_tries > 0:
        guess = guess_number()
        boolean_value = equal_variables(number, guess)
        if not boolean_value:
            print('Wrong, try again!')
            number_of_tries -= 1

    if number_of_tries > 0:
        print('You won {} points.'.format(number_of_tries))
    else:
        print('You lost. Correct answer: {}.'.format(number))
