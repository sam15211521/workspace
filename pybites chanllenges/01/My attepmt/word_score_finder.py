from scores import DICTIONARY

def score_each_word(LETTER_SCORE): # reads each line/word in DICTIONARY.txt and saves the word with the higest value to highest_vale then returns the word with the highest value as well as its score
    highest_value_word = ''
    highest_value_word_score = 0
    with open(DICTIONARY, 'r',newline = '\n') as dic:
        for word in dic.readlines():

            temp_score = score_calculation(num_of_letters(word), LETTER_SOCRES=LETTER_SCORE)
            if temp_score > highest_value_word_score:
                highest_value_word = word
                highest_value_word_score = temp_score

    return([highest_value_word, highest_value_word_score])
            



def find_the_word(word): #searches DICTIONARY for a word returns true if word in DICTIONARY else false
    with open(DICTIONARY, 'r') as dic:
        if word in dic.read():
            return True
        else:
            return False


def num_of_letters(word): # determines how many of each letter is in a word returns a dict of (letter : num of that letter)
    dict_of_letters = {}
    for letter in word:
        if letter not in dict_of_letters:
            dict_of_letters[letter] = 1
        else:
            dict_of_letters[letter] += 1
    return dict_of_letters

def score_calculation(dict_of_letters, LETTER_SOCRES): # takes a dict_of_letter, and the LETTER_SCORES dict and returns a number that is associated with that score
    score = 0

    for letter in dict_of_letters:
        if letter != '\n' and letter != '-':
            score += LETTER_SOCRES[letter.upper()] * dict_of_letters[letter]
    return score



def main():
    DICTIONARY = 'dictionary.txt'

    scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                       (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
    LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                     for letter in letters.split()}
    
    print(score_each_word(LETTER_SCORE=LETTER_SCORES))



main()
    