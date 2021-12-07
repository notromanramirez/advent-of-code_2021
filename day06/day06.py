# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code, Day 06: Lanternfish

#%% LONG INPUT
my_input = []
with open('input_copy.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '3,4,3,1,2'
    ]

#%% PART 1 CODE

lanternfish = [int(i) for i in my_input[0].split(',')]

days = 18
for day in range(days):
    
    lanternfish = [i - 1 for i in lanternfish]
    
    for i in range(len(lanternfish)):
        if lanternfish[i] == -1:
            lanternfish[i] = 6
            lanternfish.append(8)
    
    # print(day + 1, lanternfish)
    
print(len(lanternfish))


#%% PART 2 CODE

lanternfish = [int(i) for i in my_input[0].split(',')]

fishionary = {}
for i in range(8 + 2):
    fishionary[i] = 0

'''
fishionary[0] = 0
fishionary[1] = 0
fishionary[2] = 0
fishionary[3] = 0
fishionary[4] = 0
fishionary[5] = 0
fishionary[6] = 0
fishionary[7] = 0
fishionary[8] = 20
fishionary[9] = 0
'''

for fish in lanternfish:
    fishionary[fish] += 1
    
# print(0, fishionary)
    
days = 256
for day in range(days):
    fuckin_fish = fishionary[0]
    for i in range(8 + 1):
        fishionary[i] = fishionary[i+1]
    fishionary[6] += fuckin_fish
    fishionary[8] += fuckin_fish

    # print(day + 1, fishionary)
    
total_fish = 0
for i in range(8 + 1):
    total_fish += fishionary[i]

print(total_fish)