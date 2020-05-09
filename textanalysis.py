# Text-Analysis by Christopher Aram Swayne

# View ReadMe for more project information
from functools import reduce
from math import log2
from collections import defaultdict

FILENAME = "WarAndPeace.txt"
ALLOWED_CHARACTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                      'p','q','r','s','t','u','v','w','x','y','z',' ','A','B','C',
                      'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                      'S','T','U','V','W','X','Y','Z'
                      ]

def filter_characters(str_list):
    for ch in str_list:
        if ch in ALLOWED_CHARACTERS:
            return True

def count_occurences(str_list):
    char_dict = defaultdict(int)

    for ch in str_list:
        if ch in ALLOWED_CHARACTERS:
            char_dict[ch] += 1

    return char_dict



def text_analysis():
    # Pulls the raw text from file and places it in an array
    raw_text = str(list(open(FILENAME, 'r').read()))
    print("Test of count_occurences: " + str(dict(count_occurences(raw_text))))

text_analysis()
