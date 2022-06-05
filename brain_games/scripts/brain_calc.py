#!/usr/bin/env python3

import prompt

import numexpr as ne

from random import randint, choice


def calc_games():
    """generates a random mathematical expression and asks the user
    for the result of this expression."""

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    i = 3

    while i > 0:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        operators = ['+', '-', '*']
        operator = choice(operators)
        expression = f'{num_1} {operator} {num_2}'
        cor = ne.evaluate(f'{expression}')
        print(f'Question: {num_1} {operator} {num_2}')
        answer = int(prompt.string("Your answer: "))

        if cor == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{cor}'.")
            print(f"Let's try again, {name}!")
            break
        i -= 1

        if i == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    calc_games()
