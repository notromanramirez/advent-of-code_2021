# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 14: Extended Polymerization
    
#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C'
    ]

#%% PART 1 CODE

# initialization

polymer = my_input[0]
rules = dict()

for line in my_input[2:]:
    
    pair, insert = line.split(' -> ')
    rules[pair] = insert

# setps / algorithm
steps = 10

for i in range(steps):
    polymer_synth = polymer[0]
    for x in range(1, len(polymer)):
        polymer_synth += rules[polymer[x-1]+polymer[x]]
        polymer_synth += polymer[x]
    polymer = polymer_synth

# solve for number
freq = dict()
for char in polymer:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
        
mce = max(freq.values())
lce = min(freq.values())

# print(freq)
print(mce - lce)

#%% PART 2 CODE: DON'T MAKE THE STRING BUT COUNT THE NUMBERS

# initialization

polymer = my_input[0]
rules = dict()

for line in my_input[2:]:
    
    pair, insert = line.split(' -> ')
    rules[pair] = insert
    
# steps / algorithm : don't make the string just count the numbers

steps = 40

pairs = {symbol: 0 for symbol in rules}

def inc_dict(d):
    d_inc = {symbol: 0 for symbol in rules} 
    
    for symbol in d:
        mid = rules[symbol]
        
        d_inc[symbol[0]+mid] += d[symbol]
        d_inc[mid+symbol[1]] += d[symbol]

    return d_inc

for x in range(1, len(polymer)):
    pairs[polymer[x-1]+polymer[x]] += 1

for i in range(steps):
    pairs = inc_dict(pairs)
    
   
# convert total pairs to total elements    
elements = dict()

for k, v in pairs.items():
    if k[0] not in elements.keys():
        elements[k[0]] = v / 2
    else:
        elements[k[0]] += v / 2
                 
    if k[1] not in elements.keys():
        elements[k[1]] = v / 2
    else:
        elements[k[1]] += v / 2
        
elements[polymer[0]] += 0.5
elements[polymer[-1]] += 0.5
        
elements = {k: int(v) for k, v in elements.items()}

mce = max(elements.values())
lce = min(elements.values())

# print(elements)
print(mce - lce)
