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
    
    def add_blacklist(self, word: int, positions: list[int]):
        for pos in positions:
            if word[pos] in self.corrects or word[pos] in self.wrong_spots:
                continue

            self.blacklist.append(self.word[pos])

    def add_correct(self, word: str, positions: int):
        for pos in positions:
            if word[pos] in self.blacklist:
                self.blacklist.pop(self.blacklist.pos(word[pos]))

            # TODO: multiple values of correct poses
            self.corrects[word[pos]] = pos
    
    def add_wrong_spot(self, word: str, positions: int):
        for pos in positions:
            # remove current word if in blacklist
            if word[pos] in self.blacklist:
                self.blacklist.pop(self.blacklist.pos(word[pos]))

            if word[pos] not in self.wrong_spots:
                self.wrong_spots[word[pos]] = []

            self.wrong_spots[word[pos]].append(pos)

    def load_words(self, path: str) -> list[str]:
        return open(path, "r").read().splitlines()
    
    def get_unique_word(self) -> str:
        word = random.choice(self.words)

        if len(word) != len(set(word)):
            return self.get_unique_word()
        
        return word