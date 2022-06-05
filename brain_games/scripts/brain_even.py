#!/usr/bin/env python3

import prompt

from random import randint


def even_games():
    """Shows the player a random number. The player must enter the answer 'yes'
    if the number is even, or 'no' if it is odd."""

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 3

    while i > 0:
        num = randint(1, 100)

        print(f'Question: {num}')

        answer = prompt.string('Your answer: ')

        if num % 2 == 0 and answer == 'yes' or num % 2 != 0 and answer == 'no':
            print('Correct!')

        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'")
            print(f"Let's try again, {name}!")
            break
        i -= 1

        if i == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    even_games()
