from stats import number_of_words, number_of_characters, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    filepath = "books/frankenstein.txt"
    doc = get_book_text(filepath)
    num_words = number_of_words(doc)
    chars = number_of_characters(doc)
    refined_chars = sort_dictionary(chars)
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    #print(f"{num_words} words found in the document")
    for item in refined_chars:
        if(item["char"].isalpha()): print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()