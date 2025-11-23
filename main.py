import sys

def get_book_text(filepath):
        
        with open(filepath) as f:
        
            return f.read()

from stats import get_num_words
from stats import each_character 
from stats import sort_characters


def main():

        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        
        
        book_path = sys.argv[1]
    
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")

        char_counts = each_character(book_text)
        characters_sorted = sort_characters(char_counts)

        print("--------- Character Count -------")
        for item in characters_sorted:
            char = item["char"]
            num = item["num"]
            if not char.isalpha():
                continue
            print(f"{char}: {num}")
        print("============= END ===============")
main()

