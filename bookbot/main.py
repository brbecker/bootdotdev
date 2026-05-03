from stats import get_num_words, get_character_frequency

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main() -> None:
    text = get_book_text("books/frankenstein.txt")
    words = get_num_words(text)
    print(f"Found {words} total words")
    print(get_character_frequency(text))

main()
