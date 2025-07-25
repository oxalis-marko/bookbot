from stats import number_of_words, number_of_characters

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    doc = get_book_text("books/frankenstein.txt")
    num_words = number_of_words(doc)
    chars = number_of_characters(doc)
    print(f"{num_words} words found in the document")
    print(chars)

main()