#!/usr/bin/env python3

import random
import argparse
from . import filter as ws_filter

def ws_load_words(path: str) -> list[str]:
    return open(path, "r").read().splitlines()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="wordle_solver.py",
            description="wordle solver")

    parser.add_argument("-d", "--data", metavar="path", help="text database")
    parser.add_argument("-r", "--random", default=False, action="store_true", help="get random word")

    opts = parser.parse_args()

    words_path = opts.data if opts.data is not None else "data/example.txt"
    words = ws_load_words(words_path)

    if opts.random:
        print(random.choice(words))
        exit(0)

    blacklist = ["b", "l", "r", "e", "g"]
    corrects = {
        "s": 0,
        "m": 3,
        # "e": 3,
        # "l": 4,
    }
    wrong_spots = {
        "a": [1, 0, 4],
        "s": [2, 3],
        "i": [3, 2, 1],
    }

    words = ws_filter.has(words, [char for char in wrong_spots])
    words = ws_filter.correct_alphabets(words, corrects)
    words = ws_filter.blacklist_alphabets(words, blacklist)
    words = ws_filter.wrong_spot(words, wrong_spots)

    for w in words:
        print(w)
