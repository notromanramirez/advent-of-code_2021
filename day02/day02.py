# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code, Day 1

#%% LONG INPUT

my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line)

#%% EXAMPLE INPUT 
my_input = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
    ]

#%% PART 1 CODE

horizontal = 0
depth = 0

for instruction in my_input:
    direction, distance = instruction.split(' ')
    
    if (direction == 'forward'):
        horizontal += distance
    elif (direction == 'down'):
        depth += distance
    elif (direction == 'up'):
        depth -= distance

print(horizontal * depth)

#%% PART 2 CODE

horizontal = 0
depth = 0
aim = 0

for instruction in my_input:
    direction, distance = instruction.split(' ')
    
    if (direction == 'forward'):
        horizontal += int(distance)
        depth += (aim * int(distance))
    elif (direction == 'down'):
        aim += int(distance)
    elif (direction == 'up'):
        aim -= int(distance)

print(horizontal * depth)
