#!/usr/bin/env python

from argparse import ArgumentParser
from wordle_solver import WordleSolver

if __name__ == "__main__":
    argparser = ArgumentParser( prog="wordle_solver.py", description="wordle solver")
    argparser.add_argument("-d", "--data", metavar="path", default="data/example.txt", help="path to .txt full of words")
    opts = argparser.parse_args()

    ws = WordleSolver(opts.data)

    pass