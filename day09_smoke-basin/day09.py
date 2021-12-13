# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 09: Smoke Basin
    
#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678'
    ]

#%% PART 1 CODE

heights = [[int(s) for s in x] for x in my_input]

def is_low_point(x, y):
    low_accum = True
    val = heights[y][x]
    
    # check left
    if x != 0:
        left = heights[y][x-1]
        if (val - left) >= 0:
            low_accum = False
    # check right
    if x != len(heights[y]) - 1:
        right = heights[y][x+1]
        if (val - right) >= 0:
            low_accum = False
    # check up
    if y != 0:
        up = heights[y-1][x]
        if (val - up) >= 0:
            low_accum = False
    # check down
    if y != len(heights) - 1:
        down = heights[y+1][x]
        if (val - down) >= 0:
            low_accum = False
            
    return low_accum

total = 0
for y in range(len(heights)):
    for x in range(len(heights[y])):
        if (is_low_point(x, y)):
            total += heights[y][x] + 1
            
print(total)

#%% PART 2 CODE

heights = [[int(s) for s in x] for x in my_input]

def is_low_point(x, y):
    
    low_accum = True
    val = heights[y][x]
    
    # check left
    if x != 0:
        left = heights[y][x-1]
        if (val - left) >= 0:
            low_accum = False
    # check right
    if x != len(heights[y]) - 1:
        right = heights[y][x+1]
        if (val - right) >= 0:
            low_accum = False
    # check up
    if y != 0:
        up = heights[y-1][x]
        if (val - up) >= 0:
            low_accum = False
    # check down
    if y != len(heights) - 1:
        down = heights[y+1][x]
        if (val - down) >= 0:
            low_accum = False
            
    return low_accum

low_points = []

for y in range(len(heights)):
    for x in range(len(heights[y])):
        if (is_low_point(x, y)):
            low_points.append((x, y))
            
def find_non_nine(p, p_set):
    p_set.add(p)
    
    size = 1
    x, y = p
    val = heights[y][x]
    
    if x != 0:
        left = heights[y][x-1] 
    if x != len(heights[y]) - 1:     
        right = heights[y][x+1]
    if y != 0:     
        up = heights[y-1][x]
    if y != len(heights) - 1:    
        down = heights[y+1][x] 
    
    # base case
    if val == 9:
        return 0
    
    # check left
    if x != 0 and ((x - 1, y) not in p_set):
        if (val - left) != 9:
            size += find_non_nine((x-1, y), p_set)
    # check right
    if x != len(heights[y]) - 1 and ((x + 1, y) not in p_set):
        if (val - right) != 9:
            size += find_non_nine((x+1, y), p_set)
    # check up
    if y != 0 and ((x, y - 1) not in p_set):
        if (val - up) != 9:
            size += find_non_nine((x, y-1), p_set)
    # check down
    if y != len(heights) - 1 and ((x, y + 1) not in p_set):
        if (val - down) != 9:
            size += find_non_nine((x, y+1), p_set)
            
    return size
    
def start_find_non_nine(p):
    return find_non_nine(p, set([]))

basin_sizes = []
for point in low_points:
    basin_sizes.append(start_find_non_nine(point))

basin_sizes = sorted(basin_sizes)
three_largest = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
print(three_largest)
