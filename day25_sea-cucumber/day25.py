# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 25: Sea Cucumber

from collections import defaultdict

#%% GENERATED INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))
        
#%% LONG INPUT
my_input = [
    'v...>>.vv>',
    '.vv>>.vv..',
    '>>.>v>...v',
    '>>v>>.>.v.',
    'v>v.vv.v..',
    '>.>>..v...',
    '.vv..>.>v.',
    'v.v..>>v.v',
    '....v..v.>'
    ]

#%% EXAMPLE INPUT
my_input = [
    '...>...',
    '.......',
    '......>',
    'v.....>',
    '......>',
    '.......',
    '..vvv..'
    ]

#%% MEDIUM INPUT
my_input = [
    '..........',
    '.>v....v..',
    '.......>..',
    '..........'
    ]

#%% ONE-LINE INPUT
my_input = [
    '...>>>>>...'
    ]

#%% PART 1 CODE

MAX_X, MAX_Y = len(my_input[0]), len(my_input)

def print_board(b):
    for y in range(MAX_Y):
        line = ''
        for x in range(MAX_X):
            line += b[x, y]
        print(line)
    print()

board = defaultdict(lambda: None)
R, D, N = '>', 'v', '.'

# initialize the board
for y, line in enumerate(my_input):
    for x, cum in enumerate(line):
        board[x, y] = cum

# print_board(board)
right_moves, down_moves = defaultdict(bool), defaultdict(bool)        
steps = 0
while (steps == 0) or ((True in right_moves.values()) or (True in down_moves.values())):

    right_moves = defaultdict(bool)

    # find eligible right cucumber movers
    for x, y in board:
        val = board[x, y]
        
        #right cucumber case
        if val == R:
            adj_x = (x + 1) % MAX_X
            adj_val = board[adj_x, y]
            if adj_val not in (R, D):
                right_moves[x, y] = True
            
        
    # moves eligible cucumber movers
    # new_board = defaultdict(lambda: N)
    for x, y in right_moves:
        val = board[x, y]
        
        # right cucumber case
        if val == R:
            adj_x = (x + 1) % MAX_X
            adj_val = board[adj_x, y]
            
            board[x, y], board[adj_x, y] = N, R
       
    down_moves = defaultdict(bool)

    # find eligible right cucumber movers
    for x, y in board:
        val = board[x, y]
            
        # down cucumber case
        if val == D:
            adj_y = (y + 1) % MAX_Y
            adj_val = board[x, adj_y]
            if adj_val not in (R, D):
                down_moves[x, y] = True
            
        
    # moves eligible cucumber movers
    # new_board = defaultdict(lambda: N)
    for x, y in down_moves:
        val = board[x, y]
            
            
        if val == D:
            adj_y = (y + 1) % MAX_Y
            adj_val = board[x, adj_y]
            
            board[x, y], board[x, adj_y] = N, D
        
    # print_board(board)
    steps += 1
    
print(f'{steps = }')