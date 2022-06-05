#!/usr/bin/env python


import brain_games.cli


def main():
    """Display an invitation to the game, asks the player for his name and
    welcomes him"""

    print("Welcome to the Brain Games!")
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
    brain_games.cli.welcome_user()
