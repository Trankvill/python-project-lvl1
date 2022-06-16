#!/usr/bin/env python

import numexpr as ne

from random import randint, choice

RULES = 'What is the result of the expression?'

START = 1
FINISH = 100


def get_round():
    """Creates a random mathematical expression and calculates its result"""

    r_num_1 = randint(START, FINISH)
    r_num_2 = randint(START, FINISH)
    operators = ['+', '-', '*']
    operator = choice(operators)
    expression = f'{r_num_1} {operator} {r_num_2}'
    correct_answer = str(ne.evaluate(f'{expression}'))
    return correct_answer, expression
