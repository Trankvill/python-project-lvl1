#!/usr/bin/env python

from brain_games.engine import launch_game

from brain_games.games import progression


def main():
    """Starts the game 'Arithmetic Progression'"""

    launch_game(progression)


if __name__ == '__main__':
    main()
