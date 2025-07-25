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

def sort_on(item):
    return item["num"]

def sort_dictionary(dic):
    dict_list = []
    for item in dic:
        char_dict = {"char": item,
                     "num": dic[item]}
        dict_list.append(char_dict)
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list
