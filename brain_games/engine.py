#!/usr/bin/env python

import prompt


def launch_game(game):
    """Greets the player and checks the player's response to the task
    in the running game. Controls the overall logic of the game."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.GAME_CONDITION)

    attempts = 3

    while attempts > 0:
        correct_answer, question = game.get_game()
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        attempts -= 1

        if attempts == 0:
            print(f'Congratulations, {name}!')
