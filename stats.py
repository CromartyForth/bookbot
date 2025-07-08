def get_num_words(text):   
    split_text = text.split()
    return len(split_text)

def get_letter_count(text):
    text = text.lower()
    letter_count = {}

    for char in text:
        if char in letter_count.keys():
            letter_count[char] = letter_count[char] +1
        else:
            letter_count[char] = 1
    return letter_count


def get_sorted_dictionary(dictionary):

    list_of_numbers = lambda items : items["num"]
    expanded_dictionary = []

    for key in dictionary.keys():
        expanded_dictionary.append({"char" : key, "num" : dictionary[key]})

    expanded_dictionary.sort(reverse=True, key=list_of_numbers )
    return expanded_dictionary
