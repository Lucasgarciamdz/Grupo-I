import nltk
from nltk.corpus import words

nltk.download('words')

# Get all English words
english_words = words.words()

# Criteria
length = 7
possible_letters = set('eiajkzvbnmt')
must_contain = set('ine')
must_end_with = 't'
not_start_with = ['in', 'en']
not_2nd_letter = 'i'
not_3rd_letter = 'n'
double_n = 'nn'
fourth_letter = 'n'
not_5th_letter = ['e', 'i']
not_6th_letter = 'n'
not_contain = set('qryuopsdghlcwfx')

# Filter words
filtered_words = [word for word in english_words if len(word) == length and all([
    set(word).issubset(possible_letters),
    must_contain.issubset(word),
    word[-1] == must_end_with,
    not any(word.startswith(ns) for ns in not_start_with),
    word[1] != not_2nd_letter,
    word[2] != not_3rd_letter,
    double_n in word,
    word[3] == fourth_letter,
    word[4] not in not_5th_letter,
    word[5] != not_6th_letter,
    not any(nc in word for nc in not_contain)
])]

print(filtered_words)