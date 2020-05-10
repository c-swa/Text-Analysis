# Text-Analysis by Christopher Aram Swayne

# View ReadMe for more project information
import time
from functools import reduce
import multiprocessing
import timeit
from math import log2

FILENAME = "WarAndPeace.txt"
ALLOWED_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C',
                      'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "'"
                      ]


def filter_characters(string):
    return filter(lambda ch: ch in ALLOWED_CHARACTERS, string)


# Counts total number of times each single character is occurring in the text
def count_s_occurrences(string):
    char_dict = {}
    for ch in string:
        char_dict.setdefault(ch, 0)
        char_dict[ch] += 1
        
    return char_dict


# Calculates the total entropy of the character dictionary (where the keys are single characters)
def get_entropy(str_dict):
    total = sum(str_dict.values())
    return reduce(lambda acc, n_c: acc + n_c,
                  map(lambda n_c: n_c * (-1) * (n_c / total) * log2(n_c / total), str_dict.values()))


# Counts the total number of pairs of characters that occur in the passed string
def count_d_occurrences(string):
    dual_dict = {}
    # dual_dict = map(lambda n: dual_dict.setdefault(string[(n - 1):(n + 1), 0]), range(1, int(len(string) / 2) - 1))

    # return dual_dict
    for index in range(1, int((len(string) / 2) - 1)):
        dual_dict.setdefault(string[(index - 1): index + 1], 0)
        dual_dict[string[(index - 1): index + 1]] += 1

    return dual_dict


# Counts the total number of triplets of characters that occur in the passed string
def count_t_occurrences(string):
    tri_dict = {}
    for index in range(1, int((len(string) / 3) - 2)):
        tri_dict.setdefault(string[index - 1:index + 2], 0)
        tri_dict[string[index - 1:index + 2]] += 1

    return tri_dict


# Performs a textual analysis of a given .txt file - FILENAME at the top of the script
def text_analysis():
    # Pulls the raw text from file and places it in an array
    raw_text = str(open(FILENAME, 'r').read())

    #    p = multiprocessing.Pool(multiprocessing.cpu_count())
    #    single_set_p = p.map(count_s_occurrences, raw_text)
    #    dual_set_p = p.map(count_d_occurrences, raw_text)
    #    tri_set_p = p.map(count_t_occurrences, raw_text)

    #    p.close()
    #    p.join()

    #   print(single_set_p)
    #   print(dual_set_p)
    #   print(tri_set_p)

    single_set_dict = dict(count_s_occurrences(raw_text))
    dual_set_dict = dict(count_d_occurrences(raw_text))
    tri_set_dict = dict(count_t_occurrences(raw_text))

    print(single_set_dict)
    # p = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = p.map(get_entropy, [single_set_dict, dual_set_dict, tri_set_dict])
    # p.close()
    # p.join()

    entropy_list = [get_entropy(single_set_dict), get_entropy(dual_set_dict), get_entropy(tri_set_dict)]
    # return result
    return entropy_list


start_time = time.process_time_ns()
print(str(text_analysis()))
fin_time = time.process_time_ns()

print("Time (f - s): " + str(fin_time - start_time))
