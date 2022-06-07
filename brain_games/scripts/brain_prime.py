#!/usr/bin/env python

from brain_games.engine import launch_game

from brain_games.games import game_prime


def main():
    """Starts the 'prime number' game"""

    launch_game(game_prime)


if __name__ == '__main__':
    main()
