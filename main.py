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

def form_dict(dict):
    new_dict = {}
    for p, v in dict.items():
        if p.isalpha():
            new_dict[p] = dict[p]
    return new_dict


def main():
    book_path = "books/frankenstein.txt"
    book_contents = get_book_contets(book_path)
    words = word_count(book_contents)
    num_of_chars = char_count(book_contents)
    formed_dict = form_dict(num_of_chars)
    report_dict = sorted(formed_dict.items(), key = lambda formed_dict: formed_dict[1], reverse = True)
    print("### Begin report of books/frankenstein.txt ###")
    print(f"{words} words found inside the document\n")
    for i, n in report_dict:
        print(f"The '{i}' character was found {n} times")
    print("### end report ###")

main()