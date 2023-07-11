import random
from . import filter

class WordleSolver():
    words: list[str] = []
    blacklist: dict[str, list[int]] = {}
    corrects: dict[str, list[int]] = {}
    wrong_spots: dict[str, list[int]] = {}

    def __init__(self, word_file_path: str):
        self.words = self.load_words(word_file_path)
    
    def solve(self) -> list[str]:
        self.words = filter.blacklist_alphabets(self.words, self.blacklist)
        self.words = filter.correct_alphabets(self.words, self.corrects)
        self.words = filter.wrong_spot(self.words, self.wrong_spots)

        return self.words
    
    def set_blacklist(self, blacklist: dict[str, list[int]]):
        for ch, positions in blacklist.items():
            if ch in self.corrects or ch in self.wrong_spots:
                continue

            self.blacklist[ch] = positions

    def set_corrects(self, corrects: dict[str, list[int]]):
        self.corrects = corrects
    
    def set_wrong_spots(self, wrong_spots: dict[str, list[int]]):
        self.wrong_spots = wrong_spots

    def load_words(self, path: str) -> list[str]:
        return open(path, "r").read().splitlines()
    
    def get_unique_word(self) -> str:
        word = random.choice(self.words)

        if len(word) != len(set(word)):
            return self.get_unique_word()
        
        return word