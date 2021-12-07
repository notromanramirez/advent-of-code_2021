# Roman Ramirz, rr8rk@virignia,edu
# Advent of Code, DAY 04


#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT

my_input = [
    '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    '', #1
    '22 13 17 11  0',
    ' 8  2 23  4 24',
    '21  9 14 16  7',
    ' 6 10  3 18  5',
    ' 1 12 20 15 19',
    '', #7
    ' 3 15  0  2 22',
    ' 9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
    '',
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    ' 2  0 12  3  7'
    ]

#%% PART 1 CODE

bingo_nums = [int(n) for n in my_input[0].split(',')]

board_init = [[int(i) for i in n.split(' ') if i != ''] for n in my_input[1:] if n != '']
    
board_nums = []
board_guess = []

for i in range(0, len(board_init), 5):
    nums_temp = [
        board_init[i+0], 
        board_init[i+1], 
        board_init[i+2], 
        board_init[i+3], 
        board_init[i+4]
        ]
    guess_temp = [
        [False for _ in range(len(board_init[i+0]))],
        [False for _ in range(len(board_init[i+1]))],
        [False for _ in range(len(board_init[i+2]))],
        [False for _ in range(len(board_init[i+3]))],
        [False for _ in range(len(board_init[i+4]))]
        ]
    
    
    [False for _ in range(len(board_init[0]))]
    board_guess.append(guess_temp)
    board_nums.append(nums_temp)
    
# iterate through the bingo_nums and do stuff

winning_board_num = False
last_num_called = False
for bingo_num in bingo_nums:
    # change the boards according to the next guess
    for i in range(len(board_nums)): # iterate through each board
        for j in range(len(board_nums[i])): # iterate through each board row
            for k in range(len(board_nums[i][j])): # iterate through each board row element
                if ((bingo_num == board_nums[i][j][k]) and (not winning_board_num)):
                    board_guess[i][j][k] = True
                    
    # horizontal checks
    for i in range(len(board_nums)): # iterate through each board
        for j in range(len(board_nums[i])): # iterate through each board row
            if (all(board_guess[i][j])):
                # print(f"Board number {i} at row {j}, horizontal check from {bingo_num}")
                if (type(winning_board_num) == bool):
                    winning_board_num = i
                    last_num_called = bingo_num
                
    # vertical checks
    for i in range(len(board_nums)): # iterate through each board
        for j in range(len(board_nums[i])): # iterate through each board row
            check_list = []
            for k in range(len(board_nums[i][j])): # iterate through each board row element
                check_list.append(board_guess[i][k][j])
            if (all(check_list)):
                # print(f"Board number {i} at column {j}, vertical check from {bingo_num}")
                if (type(winning_board_num) == bool):
                    winning_board_num = i
                    last_num_called = bingo_num

sum_accum = 0

# for row in board_nums[winning_board_num]: print(row)
# for row in board_guess[winning_board_num]: print(row)

for j in range(len(board_nums[winning_board_num])):
    for k in range(len(board_nums[winning_board_num][j])):
        if board_guess[winning_board_num][j][k] == False:
            # print(board_nums[winning_board_num][j][k], board_guess[winning_board_num][j][k])
            sum_accum += board_nums[winning_board_num][j][k]
score = sum_accum * last_num_called
print(score)

#%% PART 2 CODE

bingo_nums = [int(n) for n in my_input[0].split(',')]

board_init = [[int(i) for i in n.split(' ') if i != ''] for n in my_input[1:] if n != '']
    
board_nums = []
board_guess = []

for i in range(0, len(board_init), 5):
    nums_temp = [
        board_init[i+0], 
        board_init[i+1], 
        board_init[i+2], 
        board_init[i+3], 
        board_init[i+4]
        ]
    guess_temp = [
        [False for _ in range(len(board_init[i+0]))],
        [False for _ in range(len(board_init[i+1]))],
        [False for _ in range(len(board_init[i+2]))],
        [False for _ in range(len(board_init[i+3]))],
        [False for _ in range(len(board_init[i+4]))]
        ]
    
    
    [False for _ in range(len(board_init[0]))]
    board_guess.append(guess_temp)
    board_nums.append(nums_temp)
    
# iterate through the bingo_nums and do stuff

winners = []
last_num_called = False
for bingo_num in bingo_nums:
    # change the boards according to the next guess
    for i in range(len(board_nums)): # iterate through each board
        for j in range(len(board_nums[i])): # iterate through each board row
            for k in range(len(board_nums[i][j])): # iterate through each board row element
                if ((bingo_num == board_nums[i][j][k]) and (not last_num_called)):
                    board_guess[i][j][k] = True
                    
    # horizontal checks
    for i in range(len(board_nums)): # iterate through each board
        for j in range(len(board_nums[i])): # iterate through each board row
            if (all(board_guess[i][j])):
                # print(f"Board number {i} at row {j}, horizontal check from {bingo_num}")
                if ((len(winners) < len(board_nums)) and (i not in winners)):
                    winners.append(i)
                if ((len(winners) == len(board_nums)) and (not last_num_called)):
                    last_num_called = bingo_num
                
    # vertical checks
    for i in range(len(board_nums)): # iterate through each board
        for j in range(len(board_nums[i])): # iterate through each board row
            check_list = []
            for k in range(len(board_nums[i][j])): # iterate through each board row element
                check_list.append(board_guess[i][k][j])
            if (all(check_list)):
                # print(f"Board number {i} at column {j}, vertical check from {bingo_num}")
                if ((len(winners) < len(board_nums)) and (i not in winners)):
                    winners.append(i)
                if ((len(winners) == len(board_nums)) and (not last_num_called)):
                    last_num_called = bingo_num
                

sum_accum = 0

# for row in board_nums[winning_board_num]: print(row)
# for row in board_guess[winning_board_num]: print(row)

for j in range(len(board_nums[winners[-1]])):
    for k in range(len(board_nums[winners[-1]][j])):
        if board_guess[winners[-1]][j][k] == False:
            # print(board_nums[winners[-1]][j][k], board_guess[winners[-1]][j][k])
            sum_accum += board_nums[winners[-1]][j][k]
score = sum_accum * last_num_called
print(score)