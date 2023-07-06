#!/usr/bin/env python3

import random
import time
from typing import Set
from colorama import Fore as F
import argparse
from . import filter as ws_filter

SLEEP_INTERVAL = 0.2
blacklist: list[str] = []
corrects: dict[str, int] = {}
wrong_spots: dict[str, list[int]] = {}

def ws_load_words(path: str) -> list[str]:
    return open(path, "r").read().splitlines()

def ws_get_unique_word(words: list[str]) -> str:
    word = random.choice(words)

    if len(word) != len(set(word)):
        return ws_get_unique_word(words)

    return word

def ws_print_ascii_art():
    print(f"""{F.BLUE}                         __ __       
 .--.--.--.-----.----.--|  |  .-----.
 |  |  |  |  _  |   _|  _  |  |  -__|
 |________|_____|__| |_____|__|_____|
              __                     
 .-----.-----|  .--.--.-----.----.   
 |__ --|  _  |  |  |  |  -__|   _|   
 |_____|_____|__|\\___/|_____|__|     {F.RESET}""")

def ws_handle_input() -> str:
    return result

def ws_parse_input(word: str, input: str):
    assert len(input) == len(word)

    for idx, ch in enumerate(input):
        match ch:
            case "B":
                blacklist.append(word[idx])
            case "C":
                corrects[word[idx]] = idx
            case "W":
                if ch not in wrong_spots:
                    wrong_spots[word[idx]] = []

                wrong_spots[word[idx]].append(idx)
            case _:
                print(F.GREEN, end="")
                print(f"[*]: Unknown input {F.RED}\"{ch}\"{F.GREEN}, Exiting..")
                exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="wordle_solver.py",
            description="wordle solver")

    parser.add_argument("-d", "--data", metavar="path", default="data/example.txt", help="path to .txt full of words")

    opts = parser.parse_args()

    ws_print_ascii_art()
    print()

    print(F.GREEN, end="")
    print("[*]: Initializing words..")
    time.sleep(SLEEP_INTERVAL)
    words = ws_load_words(opts.data)

    print(f"[*]: Loaded words from {F.RED}\"{opts.data}\"")
    time.sleep(SLEEP_INTERVAL)

    print(F.GREEN, end="")
    print("[*]: Choosing first unique word..")
    time.sleep(SLEEP_INTERVAL)
    word = ws_get_unique_word(words)

    print(f"[*]: Got word {F.RED}\"{word}\"")
    print(F.GREEN, end="")
    time.sleep(SLEEP_INTERVAL)

    print(f"[*]: Assuming wordle size is {F.RED}\"{len(word)}\"")
    print(F.GREEN, end="")
    
    time.sleep(SLEEP_INTERVAL)

    print(f"[*]: Waiting for input..")
    time.sleep(SLEEP_INTERVAL)

    while len(words) > 1:
        print(F.RESET, end="")
        result = input(">> ")

        if result.startswith("!exit"):
            print(F.GREEN, end="")
            print(f"[*]: Exiting..")
            exit(0)
        elif result.startswith("!change"):
            new_word = result.split()[1]
            print(F.GREEN, end="")
            print(f"[*]: Changed word from {F.RED}\"{word}\"{F.GREEN} to {F.RED}\"{new_word}\"{F.GREEN}..")
            word = new_word
        else:
            ws_parse_input(word, result)

            words = ws_filter.has(words, [char for char in wrong_spots])
            words = ws_filter.correct_alphabets(words, corrects)
            words = ws_filter.blacklist_alphabets(words, blacklist)
            words = ws_filter.wrong_spot(words, wrong_spots)

            print(F.GREEN, end="")
            print(f"[*]: {len(words)} words left")
            for w in words:
                print(F.GREEN, end="")
                print(f"[*]: {F.RED}\"{w}\"")

        while len(result) != len(word):
            print(F.GREEN, end="")
            print(f"[*]: Wrong size of input")
            print(f"[*]: Waiting for input..")

            print(F.RESET, end="")
            result = input(">> ")

            if result.startswith("!exit"):
                print(F.GREEN, end="")
                print(f"[*]: Exiting..")
                exit(0)
            elif result.startswith("!change"):
                new_word = result.split()[1]
                print(F.GREEN, end="")
                print(f"[*]: Changed word from {F.RED}\"{word}\"{F.GREEN} to {F.RED}\"{new_word}\"{F.GREEN}..")
                word = new_word
            else:
                ws_parse_input(word, result)

                words = ws_filter.has(words, [char for char in wrong_spots])
                words = ws_filter.correct_alphabets(words, corrects)
                words = ws_filter.blacklist_alphabets(words, blacklist)
                words = ws_filter.wrong_spot(words, wrong_spots)

                print(F.GREEN, end="")
                print(f"[*]: {len(words)} words left")
                for w in words:
                    print(F.GREEN, end="")
                    print(f"[*]: {F.RED}\"{w}\"")

    if len(words) == 1:
        print(F.GREEN, end="")
        print(f"[*]: Found word {F.RED}\"{words[0]}\"")
    else:
        print(F.GREEN, end="")
        print(f"[*]: Word is not found")
