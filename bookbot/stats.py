def get_num_words(text: str) -> int:
    return len(text.split())

def get_character_frequency(text: str) -> dict[str, int]:
    freqs = {}
    for c in text.lower():
        freqs[c] = freqs.get(c, 0) + 1
    return freqs
