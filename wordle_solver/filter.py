def has(words: list[str], chars: list[str]) -> list[str]:
    def __filter(word: str) -> bool:
        for char in chars:
            if char not in word:
                return False
        return True

    return list(filter(__filter, words))

def wrong_spot(words: list[str], wrong_spots: dict[str, list[int]]) -> list[str]:
    def __filter(word: str) -> bool:
        for wrong_char, positions in wrong_spots.items():
            for position in positions:
                if word[position] == wrong_char:
                    return False
        return True

    return list(filter(__filter, words))

def blacklist_alphabets(words: list[str], chars: list[str]) -> list[str]:
    def __filter(word: str) -> bool:
        for char in chars:
            if char in word:
                return False
        return True

    return list(filter(__filter, words))

def correct_alphabets(words: list[str], chars: dict[str, int]) -> list[str]:
    def __filter(word: str) -> bool:
        for char, position in chars.items():
            if word[position] != char:
                return False
        return True

    return list(filter(__filter, words))
