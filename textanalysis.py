# Text-Analysis by Christopher Aram Swayne

# View ReadMe for more project information
import time
from functools import reduce
import multiprocessing.dummy
from math import log2

FILENAME = "WarAndPeace.txt"
ALLOWED_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C',
                      'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "'"
                      ]


def filter_characters(string):
    return str(filter(lambda ch: ch in ALLOWED_CHARACTERS, string))


# Counts total number of times each single character is occurring in the text
def count_occurrences(string: str, chunker: int) -> dict:
    p = multiprocessing.dummy.Pool(64)
    n_chunks = len(string)//chunker
    chunks = list(p.map(lambda i: string[chunker * i:chunker * i + chunker], range(n_chunks)))
    print(chunks)
    values = dict(list(p.map((lambda key: (key, chunks.count(key))), set(chunks))))
    print(values)
    return values


# Calculates the total entropy of the character dictionary (where the keys are single characters)
def get_entropy(str_dict):
    total = sum(str_dict.values())
    return reduce(lambda acc, n_c: acc + n_c,
                  map(lambda n_c: n_c * (-1) * (n_c / total) * log2(n_c / total), str_dict.values()))


# Performs a textual analysis of a given .txt file - FILENAME at the top of the script
def text_analysis():
    # Pulls the raw text from file and places it in an array
    raw_text = str(open(FILENAME, 'r').read())

    single_set_list = dict(count_occurrences(raw_text, 1))
    dual_set_list = dict(count_occurrences(raw_text, 2))
    tri_set_list = dict(count_occurrences(raw_text, 3))

    entropy_list = [get_entropy(single_set_list), get_entropy(dual_set_list), get_entropy(tri_set_list)]
    # return result
    return entropy_list


start_time = time.process_time()
print(str(text_analysis()))
fin_time = time.process_time()

print("Time (f - s): " + str(fin_time - start_time))
