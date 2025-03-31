def get_word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    characters = text.lower()
    text_dict = {}

    for char in characters:
        text_dict[char] = text_dict.get(char, 0) + 1
    return text_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict.get(char)})
    
    list.sort(reverse=True, key=sort_on)
    return list