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


def filter_characters(string):
    for ch in string:
        if ch in ALLOWED_CHARACTERS:
            return True


# Counts total number of times each single character is occurring in the text
def count_s_occurrences(string):
    char_dict = {}
    for ch in string:
        char_dict.setdefault(ch, 0)
        char_dict[ch] += 1

    return char_dict


# Calculates the total entropy of the character dictionary (where the keys are single characters)
def get_entropy(str_dict):
    total = sum_dict(str_dict)
    summation = 0
    for ch in str_dict.keys():
        n_c = str_dict[ch]
        p_c = n_c / total
        equation = n_c * (-1) * p_c * log2(p_c)
        summation += equation

    return summation


# Counts the total number of pairs of characters that occur in the passed string
def count_d_occurrences(string):
    dual_dict = {}
    for index in range(1, int((len(string) / 2) - 1)):
        dual_dict.setdefault(string[(index - 1): index + 1], 0)
        dual_dict[string[(index - 1): index + 1]] += 1

    return dual_dict


# Counts the total number of triplets of characters that occur in the passed string
def count_t_occurrences(string):
    tri_dict = {}
    for index in range (1, int((len(string) / 3) - 2)):
        tri_dict.setdefault(string[index-1:index+2], 0)
        tri_dict[string[index - 1:index+2]] += 1

    return tri_dict


# Calculates the sum of values of a dictionary
def sum_dict(ch_dict):
    summation = 0
    for key in ch_dict.keys():
        summation += ch_dict[key]
    return summation


# Performs a textual analysis of a given .txt file - FILENAME at the top of the script
def text_analysis():
    # Pulls the raw text from file and places it in an array
    raw_text = str(open(FILENAME, 'r').read())

    single_set_dict = dict(count_s_occurrences(raw_text))
    dual_set_dict = dict(count_d_occurrences(raw_text))
    tri_set_dict = dict(count_t_occurrences(raw_text))

    entropy_list = [get_entropy(single_set_dict),get_entropy(dual_set_dict),get_entropy(tri_set_dict)]
    return entropy_list


print(str(text_analysis()))