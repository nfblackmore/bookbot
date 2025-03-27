import sys
from stats import get_num_words, count_characters, sort_counts

def get_book_text(file_path) -> str:
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    char_count = count_characters(text)
    sorted_counts = sort_counts(char_count)
    print("--------- Character Count -------")
    for sub_dict in sorted_counts:
        if sub_dict["char"].isalpha():
            char = sub_dict["char"]
            count = sub_dict["count"]
            print(f"{char}: {count}")
    print("============= END ===============")


main()