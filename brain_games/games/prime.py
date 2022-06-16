#!/usr/bin/env python

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

START = 1
FINISH = 100


def is_prime(r_num):
    """Checks whether a random number is prime"""

    count = 2

    while r_num % count != 0:
        count += 1
    return r_num == count


def get_round():
    """Calculates the correct answer"""

    r_num = randint(START, FINISH)

    if is_prime(r_num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, r_num
