import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# START HERE
def load_words():
    dict_words = []
    with open(DICTIONARY, 'r') as f:
        dict_words =  list(line.strip() for line in f)
    
    return dict_words

def calc_word_value(word):
    score = 0
    for letter in word:
        score = score + LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words=None):
    'given a list of words calculate the word with max value'
    highestword = ''
    highestscore = 0
    for word in words:
        score = calc_word_value(word)
        if score > highestscore:
            highestscore = score
            highestword = word
    
    return highestword
