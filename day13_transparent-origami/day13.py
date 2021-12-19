# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 13: Transparent Origami

#%% LONG INPUT
my_input = []
with open('input_roman.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
    ]

#%% PART 1 AND 2 CODE

class Point():
    
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
        
    def equals(self, x, y):
        return (self.x == x) and (self.y == y)
        
class Fold():
    
    def __init__(self, axis, val):
        self.axis, self.val = axis, int(val)
    

class Paper(list):
    
    def __init__(self):
        
        super().__init__()
                    
        self.x_size, self.y_size = 0, 0
        
    def __str__(self):
        total = ''
        
        for point in self:
            total += f"({point.x}, {point.y})\n"
        
        return total
    
    def display(self):
        for y in range(self.y_size + 1):
            accum = ''
            for x in range(self.x_size + 1):
                if any([p.equals(x, y) for p in self]):
                    accum += '#'
                else:
                    accum += '.'
            print(accum)
    
    def fold_paper(self, fold):
        if fold.axis == 'x':
            for point in self:
                if point.x > fold.val:
                    point.x = (2 * fold.val) - point.x
            self.x_size = int((self.x_size - 1) / 2)
            
        elif fold.axis == 'y':
            for point in self:
                if point.y > fold.val:
                    point.y = (2 * fold.val) - point.y
            self.y_size = int((self.y_size - 1) / 2)
                
    def dot_count(self):
        unique = set()
        for point in self:
            unique.add((point.x, point.y))
        return len(unique)
        
p = Paper()
f = []
        
for line in my_input:
    if len(line) > 0:
        if line.find('fold') == -1:
            x, y = line.split(',')
            p.append(Point(int(x), int(y)))
        else:
            axis, val = line[len('fold along '):].split('=')
            f.append(Fold(axis, val))
            
p.x_size = max([s.x for s in p])
p.y_size = max([s.y for s in p])

for fold in f:
    p.fold_paper(fold)

print(p.dot_count())
p.display()
