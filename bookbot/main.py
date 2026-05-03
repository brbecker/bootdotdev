from stats import get_num_words

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main() -> None:
    text = get_book_text("books/frankenstein.txt")
    words = get_num_words(text)
    print(f"Found {words} total words")

main()
