#!/usr/bin/env python


import prompt


def welcome_user():
    """Asks the player for his name and welcomes him"""

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
