#!/usr/bin/env python

from random import randint, choice

GAME_RULE = 'What number is missing in the progression?'

START = 1
FINISH = 50
START_DIFFERENCE = 1
FINISH_DIFFERENCE = 10


def get_arithmetic_sequence(arithmetic_sequence, length, r_num, difference):
    """Creates an arithmetic sequence"""

    while length < 10:
        length += 1
        r_num += difference
        arithmetic_sequence.append(r_num)
    return arithmetic_sequence


def arithmetic_sequence_str(arithmetic_sequence, secret_element):
    """Creates a string representation of an arithmetic sequence"""

    arithmetic_sequence[arithmetic_sequence.index(secret_element)] = '..'
    string_of_arithmetic_sequence = ' '.join(map(str, arithmetic_sequence))
    return string_of_arithmetic_sequence


def get_round():
    """Calculates the correct answer"""

    r_num = randint(START, FINISH)
    difference = randint(START_DIFFERENCE, FINISH_DIFFERENCE)
    arithmetic_sequence = []
    length = 0
    secret_element = choice(
        get_arithmetic_sequence(arithmetic_sequence, length, r_num, difference)
    )
    question = arithmetic_sequence_str(arithmetic_sequence, secret_element)
    correct_answer = str(secret_element)
    return correct_answer, question
