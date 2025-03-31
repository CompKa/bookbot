import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_word_count
from stats import char_count
from stats import sort_on      
from stats import sort_dict










def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    

    character_count = char_count(book_text)
    list = sort_dict(character_count)






    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list:
        letter = dict["char"]
        if letter.isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")





main()
