#!/usr/bin/env python

import prompt


NUMBER_OF_ROUNDS = 3


def launch_game(game):
    """Greets the player and checks the player's response to the task
    in the running game. Controls the overall logic of the game."""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.GAME_RULE)

    for i in range(NUMBER_OF_ROUNDS):
        correct_answer, question = game.get_round()
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
        elif answer != correct_answer:
            return print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.
Let's try again, {name}!""")

    print(f'Congratulations, {name}!')
