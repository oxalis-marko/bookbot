def number_of_words(doc):
    words = doc.split()
    return len(words)

def number_of_characters(doc):
    lower_case_doc = doc.lower()
    dif_chars = {}
    for char in lower_case_doc:
        if (char in dif_chars): dif_chars[char] += 1
        else: dif_chars[char] = 1
    return dif_chars