import sys

from stats import character_count, chars_dict_to_sorted_list, get_book_text, word_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_total = word_count(book_text)
    character_counts = character_count(book_text)
    sorted_character_counts = chars_dict_to_sorted_list(character_counts)
    print_report(book_path, word_total, sorted_character_counts)

def print_report(book_path, word_total, sorted_character_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")
    print("--------- Character Count -------")
    for char, count in sorted_character_counts:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
