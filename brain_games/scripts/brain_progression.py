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
        random_num = randint(1, 50)
        progression_step = randint(1, 10)
        progression_list = []
        progression_length = 0
        secret_element = 0
        while progression_length < 10:
            progression_length += 1
            random_num += progression_step
            progression_list.append(random_num)
            secret_element = choice(progression_list)
        progression_list[progression_list.index(secret_element)] = '..'
        secret_element = str(secret_element)
        question = ' '.join(map(str, progression_list))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == secret_element:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{secret_element}'.")
            print(f"Let's try again, {name}!")
            break
        attempts -= 1

        if attempts == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    progression_games()
