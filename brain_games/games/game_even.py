#!/usr/bin/env python

from random import randint

GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'

START = 1
FINISH = 100


def get_question():
    """Generates a random number"""

    r_num = randint(START, FINISH)
    return r_num


def get_game():
    """Checks the number for parity and writes the correct result"""

    r_num = get_question()
    if r_num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return str(result), str(r_num)
