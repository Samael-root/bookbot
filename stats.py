def get_num_words(text):

    words = text.split()
    return len(words)

def each_character(text):
    chars = {}
    text = text.lower()

    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on_num(item):
    return item["num"]

def sort_characters(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on_num)
    return sorted_list