import sys
from stats import num_of_words, character_count, sort_character_dictionary

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_contents = get_book_text(path)
    book_word_count = num_of_words(book_contents)
    num_characters_in_book = character_count(book_contents)
    sorted_characters = sort_character_dictionary(num_characters_in_book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words.")
    print("--------- Character Count -------")

    for item in sorted_characters:
        if item['char']:
                print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()


