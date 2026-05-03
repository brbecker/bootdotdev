from typing import Literal

def get_num_words(text: str) -> int:
    return len(text.split())

def get_character_frequency(text: str) -> dict[str, int]:
    freqs = {}
    for c in text.lower():
        freqs[c] = freqs.get(c, 0) + 1
    return freqs

name_or_num = Literal["name"] | Literal["num"]

def sort_on(items: dict[name_or_num, str | int]) -> list[int]:
    return items["num"]

def freqs_rev_sorted(freqs: dict[str, int]) -> list[dict[name_or_num, str | int]]:
    result = []
    for (c, num) in freqs.items():
        result.append({"name": c, "num": num})
    result.sort(reverse=True, key=sort_on)
    return result
