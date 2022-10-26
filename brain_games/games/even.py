#!/usr/bin/env python

from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

START = 1
FINISH = 100


def is_even(r_num):
    """Checks if a number is even"""

    if r_num % 2 == 0:
        return True
    else:
        return False


def get_round():
    """Calculates the correct answer(even)"""

    r_num = randint(START, FINISH)

    if is_even(r_num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, r_num
