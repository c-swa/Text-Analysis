# Text-Analysis by Christopher Aram Swayne

# View ReadMe for more project information
from functools import reduce
from math import log2
from collections import defaultdict

FILENAME = "WarAndPeace.txt"
ALLOWED_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C',
                      'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "'"
                      ]


def filter_characters(str_list):
    for ch in str_list:
        if ch in ALLOWED_CHARACTERS:
            return True


# Counts total number of times each single character is occurring in the text
def count_s_occurrences(str_list):
    char_dict = {}
    for ch in str_list:
        char_dict.setdefault(ch, 0)
        char_dict[ch] += 1

    return char_dict


# Calculates the total entropy of the single character set
def get_s_entropy(str_dict):
    total = sum_text(str_dict)
    summation = 0
    for ch in str_dict.keys():
        n_c = str_dict[ch]
        p_c = n_c / total
        equation = n_c * (-1) * (p_c) * log2(p_c)
        summation += equation

    return summation


def sum_text(ch_dict):
    total = 0
    for key in ch_dict.keys():
        total += ch_dict[key]
    return total


def text_analysis():
    # Pulls the raw text from file and places it in an array
    raw_text = str(open(FILENAME, 'r').read())

    output = dict(count_s_occurrences(raw_text))

    print(str(get_s_entropy(output)))
    # Returns the dictionary of characters, and their count of occurrences
    return output


text_analysis()
