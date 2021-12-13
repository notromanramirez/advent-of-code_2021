# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 5: Hydrothermal Venture

#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
    ]

#%% PART 1 CODE

class Instruction:   
    
    def __init__(self, s):
        self.point1, self.point2 = s.split(' -> ')
        self.x1, self.y1 = [int(i) for i in self.point1.split(',')]
        self.x2, self.y2 = [int(i) for i in self.point2.split(',')]

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"
    
    def dx(self):
        return self.x2 - self.x1

    def dy(self):
        return self.y2 - self.y1
    
class Board(list):
    
    def __init__(self, x, y):
        super().__init__([[0 for x in range(board_x + 1)] for y in range(board_y + 1)])
    
    def __str__(self):
        accum = ''
        for row in self:
            for elem in row:
                if elem == 0:
                    accum += '.'
                else:
                    accum += str(elem)
            accum += '\n'
        return accum
        
insts = [Instruction(s) for s in my_input]

board_x = max([max(i.x1, i.x2) for i in insts])
board_y = max([max(i.y1, i.y2) for i in insts])

# initialize the board
board = Board(board_x, board_y)

for inst in insts:
    # going horizontal
    if (inst.dy() == 0):
        # print(inst)
        direction = 1 if inst.dx() > 0 else -1
        for x in range(inst.x1, inst.x2 + direction, direction):
            # print(x)
            board[inst.y1][x] += 1
    # going vertical
    elif (inst.dx() == 0):
        # print(inst)
        direction = 1 if inst.dy() > 0 else -1
        for y in range(inst.y1, inst.y2 + direction, direction):
            # print(y)
            board[y][inst.x1] += 1
            
# how many points are greater than 2?
total = 0
for row in board:
    for elem in row:
        if elem >= 2:
            total += 1
print(total)

#%% PART 2 CODE

class Instruction:   
    
    def __init__(self, s):
        self.point1, self.point2 = s.split(' -> ')
        self.x1, self.y1 = [int(i) for i in self.point1.split(',')]
        self.x2, self.y2 = [int(i) for i in self.point2.split(',')]

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"
    
    def dx(self):
        return self.x2 - self.x1

    def dy(self):
        return self.y2 - self.y1
    
class Board(list):
    
    def __init__(self, x, y):
        super().__init__([[0 for x in range(board_x + 1)] for y in range(board_y + 1)])
    
    def __str__(self):
        accum = ''
        for row in self:
            for elem in row:
                if elem == 0:
                    accum += '.'
                else:
                    accum += str(elem)
            accum += '\n'
        return accum
        
insts = [Instruction(s) for s in my_input]

board_x = max([max(i.x1, i.x2) for i in insts])
board_y = max([max(i.y1, i.y2) for i in insts])

# initialize the board
board = Board(board_x, board_y)

for inst in insts:
    # going horizontal
    if (inst.dy() == 0):
        # print(inst)
        direction = 1 if inst.dx() > 0 else -1
        for x in range(inst.x1, inst.x2 + direction, direction):
            # print(x)
            board[inst.y1][x] += 1
    # going vertical
    elif (inst.dx() == 0):
        # print(inst)
        direction = 1 if inst.dy() > 0 else -1
        for y in range(inst.y1, inst.y2 + direction, direction):
            # print(y)
            board[y][inst.x1] += 1
    # going diagonal
    else:
        x_dir = 1 if inst.dx() > 0 else -1
        y_dir = 1 if inst.dy() > 0 else -1
        
        for i in range(max(abs(inst.dx()), abs(inst.dy())) + 1):
            board[inst.y1 + (i * y_dir)][inst.x1 + (i * x_dir)] += 1
        
            
# how many points are greater than 2?
total = 0
for row in board:
    for elem in row:
        if elem >= 2:
            total += 1
print(total)