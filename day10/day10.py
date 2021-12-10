# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 10: Syntax Scoring
    
#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
    ]

#%% PARTS 1 AND 2 BECAUSE IT INVOLES THE SAME ALGORITHM: FINISHED AT 12:40 AM

points_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
    }
points_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
    }
occurs = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
    }

opens = ('(', '[', '{', '<')
closes = (')', ']', '}', '>')

leftover_stack = []

for line in my_input:
    stack = []
    corrupted = False
    
    for char in line:
        
        if char in opens:
            stack.append(char)
            
        elif char in closes:
            last = stack.pop()
            i = closes.index(char)
            
            if last != opens[i]:
                # print(line, '- Expected', closes[opens.index(last)], 'but found', closes[i], 'instad.')
                occurs[closes[i]] += 1
                corrupted = True
                break
            
    if not corrupted:
        leftover_stack.append(stack)
        
total_1 = 0        
for close in closes:
    total_1 += points_1[close] * occurs[close]
print(total_1)

total_2 = []
for line in leftover_stack:
    line_total = 0
    
    for i in range(len(line) - 1, -1, -1):
        line_total *= 5
        line_total += points_2[closes[opens.index(line[i])]]
    total_2.append(line_total)

sorted_total = sorted(total_2)
print(sorted_total[int(len(sorted_total)/2)])
