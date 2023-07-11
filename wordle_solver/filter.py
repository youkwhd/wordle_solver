def wrong_spot(words: list[str], wrong_spots: dict[str, list[int]]) -> list[str]:
    def __filter(word: str) -> bool:
        for wrong_char, positions in wrong_spots.items():
            for pos in positions:
                if word[pos] == wrong_char:
                    return False

        return True

    return list(filter(__filter, words))

def blacklist_alphabets(words: list[str], chars: dict[str, list[str]]) -> list[str]:
    def __filter(word: str) -> bool:
        for char, positions in chars.items():
            if char in word:
                return False

        return True

    return list(filter(__filter, words))

def correct_alphabets(words: list[str], chars: dict[str, list[int]]) -> list[str]:
    def __filter(word: str) -> bool:
        for char, positions in chars.items():
            for pos in positions:
                if word[pos] != char:
                    return False

        return True

    return list(filter(__filter, words))
