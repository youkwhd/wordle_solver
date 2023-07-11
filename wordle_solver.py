#!/usr/bin/env python

from argparse import ArgumentParser
from wordle_solver import WordleSolver

__WORD_SIZE__ = 5

def parse_characters(characters: list[str]) -> dict[str, list[int]]:
    result: dict[str, list[int]] = {}

    for raw_character in characters:
        [ch, pos] = raw_character.split(":")
        pos = int(pos)

        if pos <= 0 or pos > __WORD_SIZE__:
            print("Overflow to word size")
            exit(1)
        
        if ch not in result:
            result[ch] = []
        
        result[ch].append(pos - 1)

    return result

def parse_blacklist(blacklists: list[str]) -> dict[str, list[int]]:
    return parse_characters(blacklists)

def parse_corrects(corrects: list[str]) -> dict[str, list[int]]:
    return parse_characters(corrects)

def parse_wrong_spots(wrong_spots: list[str]) -> dict[str, list[int]]:
    return parse_characters(wrong_spots)

if __name__ == "__main__":
    # TODO: remove error
    # reproduce: python worlde_solver.py -q
    argparser = ArgumentParser(prog="wordle_solver.py", description="wordle solver", add_help=False)
    argparser.add_argument("-h", "--help", action="store_true", default=False)
    argparser.add_argument("-d", "--data", metavar="path", default="data/example.txt")
    argparser.add_argument("-r", "--random", action="store_true", default=False)
    argparser.add_argument("-b", "--blacklist", nargs="*", metavar="blacklist", default=[])
    argparser.add_argument("-c", "--correct", nargs="*", metavar="corrects", default=[])
    argparser.add_argument("-w", "--wrong", nargs="*", metavar="wrong_spots", default=[])
    opts = argparser.parse_args()

    if opts.help:
        # TODO: update usage
        print("usage: wordle_solver.py [-d path] [-b blacklist] [-c corrects] [-w wrong_spots]")
        exit(0)

    ws = WordleSolver(opts.data)
    
    if opts.random:
        print(ws.get_unique_word())
        exit(0)
    
    ws.blacklist = parse_blacklist(opts.blacklist)
    ws.wrong_spots = parse_wrong_spots(opts.wrong)
    ws.corrects = parse_wrong_spots(opts.correct)

    # print(ws.blacklist)
    # print(ws.wrong_spots)
    # print(ws.corrects)

    possible_words = ws.solve()
    for word in possible_words:
        print(word)

    pass