import re

file_path = r"2023\input\01.txt"

def find_digits(text: str):
    # remove all of the non-digits from the string
    digits = re.sub('\D', '', text)
    # join the first and the last digit and return
    return int(digits[0] + digits[-1]) 


def substitute_words(text: str):
    # the replacements keep the first and last characters in tact for cases like oneight (o1ee8t)or twone (t2oo1e)
    replacements_dictionary = {
        'one':'o1e',
        'two':'t2o',
        'three':'t3e',
        'four':'f4r', 
        'five':'f5e',
        'six':'s6x',
        'seven':'sv7n',
        'eight':'e8t',
        'nine':'n9e'
    }
    # replace all of the word occurances with the modified entries
    for key, value in replacements_dictionary.items():
            text = text.replace(key, value)
    return text


def part_one():
    with open(file_path, 'r') as file:
        total = 0
        for line in file:
            total += find_digits(line)
    return total


def part_two():
    with open(file_path, 'r') as file:
        total = 0
        for line in file:
            line = substitute_words(line)
            total += find_digits(line)
        return total
    
print("Part One:", part_one())
print("Part Two:", part_two())