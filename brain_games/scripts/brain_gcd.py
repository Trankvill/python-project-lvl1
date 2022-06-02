#!/usr/bin/env python

import prompt

from random import randint


def gcd_games():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    attempts = 3

    while attempts > 0:
        num_1 = randint(1, 100)
        num_2 = randint(1, 100)
        max_num = max([num_1, num_2])
        min_num = min([num_1, num_2])
        print(f'Question: {max_num} {min_num}')
        list_correct = []

        for i in range(1, max_num):
            i_find = 0
            if max_num % i == 0 and min_num % i == 0:
                i_find = i
            list_correct.append(i_find)

        corr = max(list_correct)
        answer = prompt.string('Your answer: ')

        if int(answer) == corr:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{corr}'")
            print(f"Let's try again, {name}!")
            break
        attempts -= 1

        if attempts == 0:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    gcd_games()
