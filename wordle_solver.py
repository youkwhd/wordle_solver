#!/usr/bin/env python

from argparse import ArgumentParser
from wordle_solver import WordleSolver

if __name__ == "__main__":
    argparser = ArgumentParser(prog="wordle_solver.py", description="wordle solver", add_help=False)
    argparser.add_argument("-h", "--help", action="store_true", default=False)
    argparser.add_argument("-d", "--data", metavar="path", default="data/example.txt")
    argparser.add_argument("-b", "--blacklist", metavar="blacklist", default="")
    argparser.add_argument("-c", "--correct", metavar="corrects", default="")
    argparser.add_argument("-w", "--wrong", metavar="wrong_spots", default="")
    opts = argparser.parse_args()

    if opts.help:
        print("usage: wordle_solver.py [-d path] [-b blacklist] [-c corrects] [-w wrong_spots]")
        exit(0)

    ws = WordleSolver(opts.data)

    # for word in ws.words:
    #     print(word)

    pass