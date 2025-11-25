import sys
from stats import count_words, char_count, format_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(book))} total words")
        print("--------- Character Count -------")
        counts = format_report(char_count(get_book_text(book)))
        for char in counts:
            print(f"{char['char']}: {char['num']}")
        print("============= END ===============")

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()