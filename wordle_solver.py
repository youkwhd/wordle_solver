import wordle_solver
import signal, sys
from colorama import Fore as F
import argparse

def ws_parse_input(word: str, input: str):
    if len(input) != len(word):
        print(F.GREEN, end="")
        print(f"[*]: Input length does not match with current word..")
        return

    for idx, ch in enumerate(input):
        match ch:
            case "B":
                if word[idx] in corrects or word[idx] in wrong_spots:
                    continue

                blacklist.append(word[idx])
            case "C":
                if word[idx] in blacklist:
                    blacklist.pop(blacklist.index(word[idx]))

                # TODO: multiple values of correct indexes
                corrects[word[idx]] = idx
            case "W":
                if word[idx] in blacklist:
                    blacklist.pop(blacklist.index(word[idx]))

                if ch not in wrong_spots:
                    wrong_spots[word[idx]] = []

                wrong_spots[word[idx]].append(idx)
            case _:
                print(F.GREEN, end="")
                print(f"[*]: Unknown input {F.RED}\"{ch}\"{F.GREEN}, Exiting..")
                exit(1)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser( prog="wordle_solver.py", description="wordle solver")
    argparser.add_argument("-d", "--data", metavar="path", default="data/example.txt", help="path to .txt full of words")
    opts = argparser.parse_args()

    ws = wordle_solver.WordleSolver(opts.data)
    ws.print_ascii_art()

    pass