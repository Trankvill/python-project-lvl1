#!/usr/bin/env python

import prompt

from random import randint, choice


def progression_games():
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
        elem = 0
        while a < 10:
            a += 1
            num_1 += diff
            list_t.append(num_1)
            elem = choice(list_t)
        list_t[list_t.index(elem)] = '..'
        question = ' '.join(map(str, list_t))
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if int(answer) == elem:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{elem}'")
            print(f"Let's try again, {name}")
            break
        attempts -= 1

        if attempts == 0:
            print(f'Congratulations, {name}')


if __name__ == '__main__':
    progression_games()
