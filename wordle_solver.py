#!/usr/bin/env python

from argparse import ArgumentParser as __ArgumentParser
from wordle_solver import WordleSolver

class ArgumentParser(__ArgumentParser):
    def print_help(self, file=None):
        print("Usage: wordle_solver.py [-r] [-d | --data file_path] [-b blacklist]... [-c corrects]... [-w wrong_spots]...")
        print("Yet another wordle solver.")

    def error(self, message: str):
        self.print_help()
        exit(1)


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
    argparser = ArgumentParser(prog="wordle_solver")
    argparser.add_argument("-d", "--data", metavar="path", default="data/example.txt")
    argparser.add_argument("-r", "--random", action="store_true", default=False)
    argparser.add_argument("-b", "--blacklist", nargs="*", metavar="blacklist", default=[])
    argparser.add_argument("-c", "--correct", nargs="*", metavar="corrects", default=[])
    argparser.add_argument("-w", "--wrong", nargs="*", metavar="wrong_spots", default=[])
    args = argparser.parse_args()

    ws = WordleSolver(args.data)
    
    if args.random:
        print(ws.get_unique_word())
        exit(0)
    
    ws.set_wrong_spots(parse_wrong_spots(args.wrong))
    ws.set_corrects(parse_corrects(args.correct))
    ws.set_blacklist(parse_blacklist(args.blacklist))

    possible_words = ws.solve()
    for word in possible_words:
        print(word)

    pass
