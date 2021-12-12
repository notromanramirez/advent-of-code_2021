# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 12: Passage Pathing

#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
    ]

#%% SMALLER INPUT

my_input = [
    'start-A',
    'A-b',
    'A-end'
    ]

#%% LARGER INPUT

my_input = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW'
    ]

#%% PART 1 CODE

class Instruction:
    
    def __init__(self, s):
        self.p1, self.p2 = s.split('-')
        
class Node:
    
    def __init__(self, s):
        self.s = s
        self.pointers = []
        self.is_visited = False
        
    def __str__(self):
        return self.s
        
    def is_small(self):
        return not self.s.isupper()
             
insts = [Instruction(s) for s in my_input]

node_names = set()
for i in insts:
    node_names.add(i.p1)
    node_names.add(i.p2)
    
node_names = tuple(node_names)
    
nodes = {s: Node(s) for s in node_names}

for i in insts:
    if i.p2 != 'start':
        nodes[i.p1].pointers.append(nodes[i.p2])
    if i.p1 != 'start':
        nodes[i.p2].pointers.append(nodes[i.p1])
        
nodes['end'].pointers = []

all_paths = []

def traverse(n, path):

    if n.is_small() and n.s != 'end':
        n.is_visited = True
        
    if n.s == 'end':
        all_paths.append([m.s for m in path] + [n.s])
        
    for child in n.pointers:
        if not child.is_visited == True:
            traverse(child, path + [n])
            child.is_visited = False
     
def start_traverse(): 
    return traverse(nodes['start'], [])

start_traverse()
print(len(all_paths))

#%% PART 2 CODE

class Instruction:
    
    def __init__(self, s):
        self.p1, self.p2 = s.split('-')
        
class Node:
    
    def __init__(self, s):
        self.s = s
        self.pointers = []
        self.visits = 0
        
    def __str__(self):
        return self.s
        
    def is_small(self):
        return not self.s.isupper()
        
        
        
insts = [Instruction(s) for s in my_input]

node_names = set()
for i in insts:
    node_names.add(i.p1)
    node_names.add(i.p2)
    
node_names = tuple(node_names)
    
nodes = {s: Node(s) for s in node_names}

for i in insts:
    if i.p2 != 'start':
        nodes[i.p1].pointers.append(nodes[i.p2])
    if i.p1 != 'start':
        nodes[i.p2].pointers.append(nodes[i.p1])
        
nodes['end'].pointers = []

all_paths = []

def traverse(n, path, dt):

    if n.is_small() and n.s != 'end':
        n.visits += 1
        
    if n.visits == 2:
        dt = True
        
    if n.s == 'end':
        all_paths.append([m.s for m in path] + [n.s])
        
    if dt:
        for child in n.pointers:
            if child.visits < 1:
                traverse(child, path + [n], dt)
                child.visits -= 1
    else:
        for child in n.pointers:
            if child.visits < 2:
                traverse(child, path + [n], dt)
                child.visits -= 1
     
def start_traverse(): 
    return traverse(nodes['start'], [], False)

start_traverse()
print(len(all_paths))
