#!/usr/bin/env python

from random import randint

GAME_CONDITION = 'Find the greatest common divisor of given numbers.'

START = 1
FINISH = 100


def get_question():
    """Generates two random numbers"""

    r_num_1 = randint(START, FINISH)
    r_num_2 = randint(START, FINISH)
    return r_num_1, r_num_2


def get_game():
    """Defines the maximum and minimum number of two random numbers.
    Calculates the greatest common divisor of these numbers and records
    the correct result"""

    r_num_1, r_num_2 = get_question()
    max_num = max([r_num_1, r_num_2])
    min_num = min([r_num_1, r_num_2])
    question = f'{min_num} {max_num}'
    list_correct = []

    for i in range(1, max_num):
        num_find = 0
        if max_num % i == 0 and min_num % i == 0:
            num_find = i
        list_correct.append(num_find)
        result = max(list_correct)
    return str(result), question
