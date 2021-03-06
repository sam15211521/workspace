from data import DICTIONARY, LETTER_SCORES

def load_words(path=DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(path) as file:
        return [line.strip() for line in file]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0
    for char in word:
        total += LETTER_SCORES.get(char.upper(), 0)
    return total


def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate

