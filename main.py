import sys
from stats import get_num_words_in_string, get_character_frequencies, get_sorted_list_of_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    book_text = get_book_text(filepath)
    num_words = get_num_words_in_string(book_text)
    char_frequencies = get_character_frequencies(book_text)
    char_report = get_sorted_list_of_dicts(char_frequencies)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in char_report:
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(args[1])