file_path = r"2023\input\03.txt"

def part_one() -> int:

    symbols = '#$+@*/%&=-'
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    engine_parts_sum = 0 
    

    with open(file_path, 'r') as file:
        a = file.readlines()
        lines = [line.rstrip('\n') + ':' for line in a]

    grid = [list(line.strip()) for line in lines]
              
    num_rows = len(grid)
    num_cols = len(grid[0])
    print(num_cols)
    number = ""
    for row in range(num_rows):
        for col in range(num_cols):
            # visit the current cell
            cell = grid[row][col]
            # create a list of the cell's neighbours
            cell_neighbors = []
            # check to see if the current cell is numeric.
            if cell.isnumeric():
                # if it is numeric, add it to the current number
                number += cell
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    # check for a valid index and visit neighbours
                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                        # add the neighbour to the list of neighbours. 
                        cell_neighbors.append(grid[new_row][new_col])
                # check if a symbol occurs in the list of neighbours
                if any(c in symbols for c in cell_neighbors):
                    # add a flag if it does
                    number += 'T'
            else:
                # check if the constructed number contains the flag
                if 'T' in number:
                    # add to total
                    engine_parts_sum += (int(number.replace('T', '')))
                number = ""

    return engine_parts_sum

            
def part_two() -> int:
    answer = 0
    with open(file_path, 'r') as file:    
        total = 0
        for line in file:
            break
    print(f"Part Two: {answer}")

part_one()
# 540131
part_two()
# 86879020


print("Part One:", part_one())
print("Part Two:", part_two())