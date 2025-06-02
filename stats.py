def num_of_words(text):
    word_count = text.split()
    return len(word_count)

def character_count(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_character_dictionary(char_dict):
    char_list = []

    for char, count, in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    def sort_on(item):
        return item["num"]
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list