import sys

from stats import freqs_rev_sorted, get_character_frequency, get_num_words

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main(book: str) -> None:
    print( "============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    text = get_book_text(book)

    print( "----------- Word Count ----------")
    words = get_num_words(text)
    print(f"Found {words} total words")

    print( "--------- Character Count -------")
    freqs_sorted = freqs_rev_sorted(get_character_frequency(text))
    for freq in freqs_sorted:
        if freq['name'].isalpha():
            print(f"{freq['name']}: {freq['num']}")

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
