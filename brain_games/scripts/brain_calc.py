#!/usr/bin/env python

from brain_games.engine import launch_game

from brain_games.games import calc


def main():
    """Starts the 'Calculator' game"""

    launch_game(calc)


if __name__ == '__main__':
    main()
