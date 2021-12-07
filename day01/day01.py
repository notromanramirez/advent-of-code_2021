# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code, Day 1

#%% LONG INPUT

my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(int(line))

#%% EXAMPLE INPUT 
my_input = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263]


#%% PART 1 CODE
accum = 0
for i in range(len(my_input) - 1):
    change = my_input[i+1] - my_input[i]
    if (change > 0):
        accum += 1
        
print(accum)

#%% PART 2 CODE

accum = 0
for i in range(len(my_input) - 3):
    change = my_input[i+3] - my_input[i]
    if (change > 0):
        accum += 1

print(accum)