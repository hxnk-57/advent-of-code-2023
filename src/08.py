file_path = r"2023\input\08.txt"


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def part_one() -> int:
    file = open(file_path).read().strip()
    instructions, nodes = file.split('\n\n')

    network = {}

    for node in nodes.splitlines():
        node, values = node.split(' = ')
        left, right = values.split(',')
        network[node] = Node(left[1:], right[1:-1])

    steps = 0
    current_node = network["AAA"]
    
    while current_node != network["ZZZ"]:
        if instructions[steps % len(instructions)] == 'L':
            current_node = network[current_node.left]
        else:
            current_node = network[current_node.right]
        steps += 1
    return steps + 1



def part_two() -> int:
    steps = 0
    with open(file_path, 'r') as file:
        steps = 0
        for line in file:
            break
        
    return steps

print("Part One", part_one())
print("Part Two", part_two())
#12833235391111