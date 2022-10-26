#!/usr/bin/env python

from random import randint

RULES = 'Find the greatest common divisor of given numbers.'

START = 1
FINISH = 100


def get_gcd(min_r_num, max_r_num):
    """Calculates the greatest common divisor random numbers"""

    while min_r_num != 0 and max_r_num != 0:

        if min_r_num > max_r_num:
            min_r_num = min_r_num % max_r_num
        else:
            max_r_num = max_r_num % min_r_num
    gcd = min_r_num + max_r_num
    return gcd


def get_round():
    """Calculates the correct answer (GCD)"""

    r_num_1 = randint(START, FINISH)
    r_num_2 = randint(START, FINISH)
    max_r_num = max([r_num_1, r_num_2])
    min_r_num = min([r_num_1, r_num_2])
    question = f'{min_r_num} {max_r_num}'
    correct_answer = str(get_gcd(min_r_num, max_r_num))
    return correct_answer, question
