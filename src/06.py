#file_path = r"202_\input\0_-test.txt"

def part_one() -> int: 
    total = 1 
    races = [
        {'time': 54, 'record': 446},
        {'time': 81, 'record': 1292},
        {'time': 70, 'record': 1035},
        {'time': 88, 'record': 1007}
    ]
    
    for race in races:
        time = race['time']
        winning_strategies = 0
        for millisecond in range(0, time):
            travel_time = time - millisecond
            record_traveled = travel_time * millisecond
            if record_traveled > race["record"]:
                winning_strategies += 1          
        total *= winning_strategies

    return total


# part two can be optimized using the quadratic forumla instead of brute forcing
# find the two intersections of the curve and of the record.
# the solution range starts at the first integer greater than the smaller root (use ceiling) and ends at the last int smaller than the larger root (use floor func).
# (time - x) * x > dist
# x*time - x**2 > dist
# x**2 - x*time + dist < 0
# 
# def get_num_ways(time, dist):
#     a = 1
#     b = -time
#     c = dist
#     pr = (-b + sqrt((b) ** 2 - (4 * a * c))) / (2 * a)
#     nr = (-b - sqrt((b) ** 2 - (4 * a * c))) / (2 * a)

#     # exclude the roots if they are integers
#     offset = 1
#     if pr == floor(pr):
#         offset -= 1
#     if nr == ceil(nr):
#         offset -= 1
#     return floor(pr) - ceil(nr) + offset

def part_two() -> int:
    race_time = 54817088
    record = 446129210351007
    winning_strategies = 0 

    for millisecond in range(0, race_time):
        travel_time = race_time - millisecond
        record_traveled = travel_time * millisecond
        if record_traveled > record:
                winning_strategies += 1
       
    return winning_strategies

print("Part One:", part_one())
print("Part Two:", part_two())