def word_count(book):
    words = book.split()
    return len(words)

def get_book_contets(path):
    with open(path) as f:
        return f.read()

def char_count(book):
    chars = {}
    lowered_book = book.lower()
    for char in lowered_book:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars


def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contets(book_path)
    words = word_count(book_contents)
    num_of_chars = char_count(book_contents)
    print(num_of_chars)

main()