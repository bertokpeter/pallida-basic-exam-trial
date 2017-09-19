dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(hun_word, eng_word):
    dictionary.append({hun_word: eng_word})
    return dictionary
print(add_word("asztal", "table"))

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_hun(eng_word):
    pass

def translate_to_eng(hun_word):
    for i in dictionary:
        if hun_word in i:
            return (i[hun_word])
print(translate_to_eng("alma"))