#!/usr/bin/env python

import prompt

from random import randint, choice


def progression_games():
    """Shows the player a series of numbers forming an arithmetic progression by
    replacing any of the numbers with two dots. The player must determine this
    number."""

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    attempts = 3
    while attempts > 0:
        num_1 = randint(1, 50)
        diff = randint(1, 10)
        list_t = []
        a = 0
        el = 0  # secret element by default
        while a < 10:
            a += 1
            num_1 += diff
            list_t.append(num_1)
            el = choice(list_t)  # random selection of a secret element
        list_t[list_t.index(el)] = '..'
        el = str(el)
        question = ' '.join(map(str, list_t))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == el:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{el}'.")
            print(f"Let's try again, {name}!")
            break
        attempts -= 1

        if attempts == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    progression_games()
