# Text-Analysis by Christopher Aram Swayne

# View ReadMe for more project information
from functools import reduce


def to_upper_case(s):
    return str(s).upper()


def print_iterator(it):
    return reduce()


def analysis(line):
    print(line)


def text():
    filename = "WarAndPeace.txt"
    file = open(filename, "r")
    map_iterator = map(analysis, file.readlines())


map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)
