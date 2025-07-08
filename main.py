from stats import get_num_words, get_letter_count, get_sorted_dictionary
path = "books/frankenstein.txt"

def get_book_text(path):
    with open(f"./{path}") as f:
        file_contents = f.read()
    return file_contents


def main():
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