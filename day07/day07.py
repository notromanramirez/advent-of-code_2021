# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code, Day 7: The Treachery of Wales  

import math

#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '16,1,2,0,4,2,7,1,2,14'
    ]

#%% PART 1 CODE

crab_horz = [int(s) for s in my_input[0].split(',')]

min_cost = math.inf
for h in range(max(crab_horz)):
    cost = 0
    for n in crab_horz:
        cost += abs(n - h)
    if cost < min_cost:
        min_cost = cost
        
print(min_cost)

#%% PART 2 CODE

crab_horz = [int(s) for s in my_input[0].split(',')]

min_cost = math.inf
for h in range(max(crab_horz)):
    cost = 0
    for n in crab_horz:
        cost += sum(range(abs(n - h) + 1))
    if cost < min_cost:
        min_cost = cost
        
print(min_cost)