#!/usr/bin/env python

import prompt

from random import randint


def random_num_and_check():
    """Generates a random number and performs a check for
    the simplicity of the number"""

    random_num = randint(1, 100)
    count = 0
    for i in range(2, random_num // 2 + 1):
        if (random_num % i) == 0:
            count += 1
    if count <= 0:
        return random_num, 'yes'
    else:
        return random_num, 'no'


def prime_games():
    """Greets the player, asks a question, asks the player for
    an answer and compares it with the correct answer"""

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    attempts = 3

    while attempts > 0:
        random_var, correct_answer = random_num_and_check()
        print(f'Question: {random_var}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'!")
            print(f"Let's try again, {name}!")
            break
        attempts -= 1

        if attempts == 0:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    prime_games()
