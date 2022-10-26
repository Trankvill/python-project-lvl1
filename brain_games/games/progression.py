#!/usr/bin/env python

from random import randint

RULES = 'What number is missing in the progression?'

START = 1
FINISH = 50
START_DIFFERENCE = 1
FINISH_DIFFERENCE = 10
LENGTH_LEFT_BORDER = 5
LENGTH_RIGHT_BORDER = 10


def get_arithmetic_sequence(initial_term, difference, length):
    """Creates an arithmetic sequence"""
    arithmetic_sequence = [initial_term]
    for i in range(length):
        initial_term += difference
        arithmetic_sequence.append(initial_term)
    return arithmetic_sequence


def stringify_sequence(arithmetic_sequence, hidden_term_index):
    """Creates a string representation of an arithmetic sequence"""

    arithmetic_sequence[hidden_term_index] = '..'
    string_of_arithmetic_sequence = ' '.join(map(str, arithmetic_sequence))
    return string_of_arithmetic_sequence


def get_round():
    """Calculates the correct answer (arithmetic progression)."""

    initial_term = randint(START, FINISH)
    difference = randint(START_DIFFERENCE, FINISH_DIFFERENCE)
    length = randint(LENGTH_LEFT_BORDER, LENGTH_RIGHT_BORDER)
    arithmetic_sequence = get_arithmetic_sequence(
        initial_term,
        difference,
        length)
    random_index = randint(0, len(arithmetic_sequence) - 1)
    secret_element = arithmetic_sequence[random_index]
    question = stringify_sequence(arithmetic_sequence, random_index)
    correct_answer = str(secret_element)
    return correct_answer, question
