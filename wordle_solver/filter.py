def wrong_spot(words: list[str], wrong_spots: dict[str, list[int]]) -> list[str]:
    def __filter(word: str) -> bool:
        for wrong_char, positions in wrong_spots.items():
            if wrong_char not in word:
                return False
            
            for pos in positions:
                if word[pos] == wrong_char:
                    return False

        return True

    return list(filter(__filter, words))

def blacklist_alphabets(words: list[str], chars: dict[str, list[int]]) -> list[str]:
    def __filter(word: str) -> bool:
        # TODO: blacklist relative to position
        for char, _ in chars.items():
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
