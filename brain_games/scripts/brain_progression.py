#!/usr/bin/env python

from brain_games.engine import launch_game

from brain_games.games import game_progression


def main():
    """Starts the game 'Arithmetic Progression'"""

    launch_game(game_progression)


if __name__ == '__main__':
    main()
