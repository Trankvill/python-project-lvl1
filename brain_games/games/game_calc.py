#!/usr/bin/env python

import numexpr as ne

from random import randint, choice

GAME_CONDITION = 'What is the result of the expression?'

START = 1
FINISH = 100


def get_question():
    """Generates two random numbers and a random mathematical operator"""

    r_num_1 = randint(START, FINISH)
    r_num_2 = randint(START, FINISH)
    operators = ['+', '-', '*']
    operator = choice(operators)
    return r_num_1, r_num_2, operator


def get_game():
    """Creates a random mathematical expression and calculates its result"""

    r_num_1, r_num_2, operator = get_question()
    expression = f'{r_num_1} {operator} {r_num_2}'
    result = ne.evaluate(f'{expression}')
    return str(result), expression
