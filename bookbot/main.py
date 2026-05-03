def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def count_words(text: str) -> int:
    return len(text.split())

def main() -> None:
    text = get_book_text("books/frankenstein.txt")
    words = count_words(text)
    print(f"Found {words} total words")

main()
