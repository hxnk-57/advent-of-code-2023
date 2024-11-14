import re
from collections import defaultdict
file_path = r"2023\input\04.txt"
cards_won = 0


def part_one() -> int:
    
    with open(file_path, 'r') as file:
        answer = 0
        for line in file:
            line = line[line.index(':')+1:]
            numbers = line.split('|') 
            winning_numbers = [int(element) for element in numbers[0].split()]
            current_numbers = [int(element) for element in numbers[1].split()]

            score = 0
            for c in current_numbers:
                if c in winning_numbers:
                    if score == 0:
                        score += 1
                    else:
                        score = score * 2                    
            answer +=  score
    return answer

def get_num_set(input_list):
    return set(map(int, input_list.split()))

def part_two() -> int:
    with open(file_path, 'r') as f:
        lines = f.read().split('\n')
        copies_dict = {}
        max_card_num = len(lines)
        for line in lines:
            card_num, win_list, my_list = re.split(r': | \| ', line)
            _, card_num = card_num.split()
            card_num = int(card_num)
            win_list = get_num_set(win_list)
            my_list = get_num_set(my_list)
            copies_num = len(win_list & my_list)
            for i in range(card_num + 1, card_num + copies_num + 1):
                copies_dict[i] = copies_dict.get(i, 0) + 1 + copies_dict.get(card_num, 0)

    return sum(v for v in copies_dict.values()) + max_card_num

        

print("Part One:", part_one())
print("Part Two:", part_two())