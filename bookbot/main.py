def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main() -> None:
    print(get_book_text("books/frankenstein.txt"))

main()
