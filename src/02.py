file_path = r"2023\input\02.txt"


def part_one() -> int:
    with open(file_path, 'r') as file:
        valid_id_sum = 0
        #instead of keeping a running count of ids, use a different approach to read in the game names
        game_id = 1
        for line in file:
            game = line[line.index(':')+1:]
            sets = game.split(';')
            valid_game = True
            for set in sets:
                balls_info = set.strip().split(',')
                collection = {'red': 0, 'green': 0, 'blue': 0}
                for ball in balls_info:
                    count, color = ball.split()
                    collection[color] += int(count)               
                if (collection["green"] > 13) or (collection["red"] > 12) or (collection["blue"] > 14):
                    valid_game = False           
            if valid_game:
                valid_id_sum += game_id
            game_id += 1
    
    print(f"Part One: {valid_id_sum}")


def part_two() -> int:
    with open(file_path, 'r') as file:    
        total_power = 0
        for line in file:
            game = line[line.index(':')+1:]
            sets = game.split(';')
            
            collection = {'red': 0, 'green': 0, 'blue': 0}
            for set in sets:
                balls_info = set.strip().split(',')               
                for ball in balls_info:
                    count, color = ball.split()
                    if int(count) > int(collection[color]):
                       collection[color] = count

            total_power += (int(collection['red']) * int(collection['green']) *int( collection['blue']))

    print(f"Part Two: {total_power}")

print("Part One:", part_one())
print("Part Two:", part_two())