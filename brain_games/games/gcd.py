#!/usr/bin/env python

from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'

START = 1
FINISH = 100


def get_gcd(list_correct, min_r_num, max_r_num):
    """Calculates the greatest common divisor random numbers"""

    for i in range(1, max_r_num):
        num_find = 0
        if max_r_num % i == 0 and min_r_num % i == 0:
            num_find = i
        list_correct.append(num_find)
        result = str(max(list_correct))
    return result


def get_round():
    """Calculates the correct answer"""

    r_num_1 = randint(START, FINISH)
    r_num_2 = randint(START, FINISH)
    max_r_num = max([r_num_1, r_num_2])
    min_r_num = min([r_num_1, r_num_2])
    question = f'{min_r_num} {max_r_num}'
    list_correct = []
    correct_answer = get_gcd(list_correct, min_r_num, max_r_num)
    return correct_answer, question
