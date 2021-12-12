# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code, Day 3

#%% LONG INPUT

my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT 
my_input = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
    ]

#%% PART 1 CODE

totals = [0 for s in range(len(my_input[0]))]

for number in my_input:
    for s in range(len(number)):
        if (number[s] == '1'):
            totals[s] += 1
        elif (number[s] == '0'):
            totals[s] -= 1 

gamma_rate = int(''.join([str(int(i > 0)) for i in totals]), 2)
epsilon_rate = int(''.join([str(int(i < 0)) for i in totals]), 2) 

print(bin(gamma_rate))
print(gamma_rate * epsilon_rate)

#%% PART 2 CODE

# oxygen_generator_rating
# co2_scrubber_rating

oxy_input = my_input

for i in range(len(oxy_input[0])):
    
    total = 0
    for number in oxy_input:
        if (number[i] == '1'):
            total += 1
        elif (number[i] == '0'):
            total -= 1 
        
    if (total >= 0):
        oxy_input = [j for j in oxy_input if j[i] == '1']
    elif (total < 0):
        oxy_input = [j for j in oxy_input if j[i] == '0']
        
oxygen_generator_rating = int(oxy_input[0], 2)

co2_input = my_input

for i in range(len(co2_input[0])):
    
    total = 0
    for number in co2_input:
        if (number[i] == '1'):
            total += 1
        elif (number[i] == '0'):
            total -= 1 
        
    if (total < 0):
        co2_input = [j for j in co2_input if j[i] == '1']
    elif (total >= 0):
        co2_input = [j for j in co2_input if j[i] == '0']
        
    if (len(co2_input) == 1):
        break
        
co2_scrubber_rating = int(co2_input[0], 2)

print(oxygen_generator_rating * co2_scrubber_rating)