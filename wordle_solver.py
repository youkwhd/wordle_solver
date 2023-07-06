#!/usr/bin/env python3

import random
from typing import Dict, List

# WordWrongSpot = Dict[str, List[int]]

def ws_load_words(path: str) -> list[str]:
    return open(path, "r").read().splitlines()

def ws_filter_has(words: list[str], chars: List[str]) -> list[str]:
    def __filter(word: str) -> bool:
        for char in chars:
            if char not in word:
                return False
        return True

    return list(filter(__filter, words))

def ws_filter_wrong_spot(words: list[str], wrong_spots: Dict[str, List[int]]) -> list[str]:
    def __filter(word: str) -> bool:
        for wrong_char, positions in wrong_spots.items():
            for position in positions:
                if word[position] == wrong_char:
                    return False
        return True

    return list(filter(__filter, words))

def ws_filter_blacklist_alphabets(words: list[str], chars: list[str]) -> list[str]:
    def __filter(word: str) -> bool:
        for char in chars:
            if char in word:
                return False
        return True

    return list(filter(__filter, words))

def ws_filter_correct_alphabets(words: list[str], chars: Dict[str, int]) -> list[str]:
    def __filter(word: str) -> bool:
        for char, position in chars.items():
            if word[position] != char:
                return False
        return True

    return list(filter(__filter, words))

if __name__ == "__main__":
    words = ws_load_words("data/example.txt")
