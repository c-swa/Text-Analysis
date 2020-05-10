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


def count_s_occurrences(str_list):
    char_dict = {}
    for ch in str_list:
        char_dict.setdefault(ch, 0)
        char_dict[ch] += 1

    return char_dict


def sum(ch_dict):
    total = 0
    for key in ch_dict.keys():
        total += ch_dict[key]
    return total


def text_analysis():
    # Pulls the raw text from file and places it in an array
    raw_text = str(open(FILENAME, 'r').read())

    processed_single_char_text = dict(count_s_occurrences(raw_text))
    output_str = str(processed_single_char_text)

    print("Test of count_occurrences: " + output_str)
    print(sum(processed_single_char_text))


text_analysis()
