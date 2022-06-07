#!/usr/bin/env python


from random import randint, choice

GAME_CONDITION = 'What number is missing in the progression?'

START = 1
FINISH = 50
START_STEP = 1
FINISH_STEP = 10


def get_question():
    """Generates a random number and a random progression step"""

    r_num = randint(START, FINISH)
    progression_step = randint(START_STEP, FINISH_STEP)
    return r_num, progression_step


def get_game():
    """Creates a progression formed using an initial random number and
    a random progression step"""

    r_num, progression_step = get_question()
    progression_list = []
    progression_length = 0
    secret_element = 0
    while progression_length < 10:
        progression_length += 1
        r_num += progression_step
        progression_list.append(r_num)
        secret_element = choice(progression_list)
    progression_list[progression_list.index(secret_element)] = '..'
    secret_element = str(secret_element)
    question = ' '.join(map(str, progression_list))
    return secret_element, question
