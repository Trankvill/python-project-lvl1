#!/usr/bin/env python

from random import randint

GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

START = 1
FINISH = 2


def get_question():
    """Generates a random number"""

    r_num = randint(START, FINISH)
    return r_num


def get_game():
    """Checks whether a random number is prime and writes the correct result."""

    r_num = get_question()

    count = 0

    for i in range(2, r_num // 2 + 1):
        if (r_num % i) == 0:
            count += 1
    if r_num == 1:
        result = 'no'
    elif count <= 0:
        result = 'yes'
    else:
        result = 'no'
    return result, r_num
