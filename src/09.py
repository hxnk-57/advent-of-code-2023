file_path = r"2023\input\09.txt"


def calculate_difference(numbers: [int]) -> list[int]:
    result = []
    for i in range(0, len(numbers)-1):
        result.append(numbers[i+1] - numbers[i])
    return result


def part_one() -> int:
    total = 0
    file = open(file_path).read()
    lines = file.split('\n')
    for line in lines:
        values = []
        values.append(list(map(int, line.split(" "))))
        i = 0
        while not all(element == 0 for element in values[-1]):
            values.append(calculate_difference(values[i]))
            total += values[i][-1]
            i += 1
    return total


def part_two() -> int:
    total = 0
    file = open(file_path).read()
    lines = file.split('\n')
    for line in lines:
        values = []
        values.append(list(map(int, line.split(" "))))
        i = 0
        while not all(element == 0 for element in values[-1]):
            values.append(calculate_difference(values[i]))
            i += 1
        running_count = 0
        for value in reversed(values):
            running_count =  value[0] - running_count
    
        total += running_count
    return total


print(f"Part one:", part_one())
print(f"Part Two:", part_two())