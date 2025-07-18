import sys
from stats import get_num_words, get_letter_count, get_sorted_dictionary

def get_book_text(path):
    with open(f"./{path}") as f:
        file_contents = f.read()
    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        path = sys.argv[1]

        text = get_book_text(path)
        num_words = get_num_words(text)
        letter_count = get_letter_count(text)
        sorted_dictionary = get_sorted_dictionary(letter_count)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for entry in sorted_dictionary:
            if entry["char"].isalpha():
                print(f"{entry["char"]}: {entry["num"]}")
        print("============= END ===============")



main()