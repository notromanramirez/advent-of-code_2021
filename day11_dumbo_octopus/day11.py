# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 11: Dumbo Octopus
    
#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526'
    ]

#%% EXAMPLE INPUT 2
my_input = [
    '11111',
    '19991',
    '19191',
    '19991',
    '11111',
    ]


#%% PART 1 CODE

class Octopus:   
    
    def __init__(self, i):
        self.value = int(i)
        self.has_flashed = False

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value) + ',' + str(int(self.has_flashed))
        

octopi = [[Octopus(s) for s in line] for line in my_input]

def oprint(i=0):
    print(i)
    for line in octopi:
        print([str(o) for o in line])

total_flashes = 0

steps = 100
oprint()
for i in range(1, steps+1):
        
    # First, the energy level of each octoups increases by 1
    
    for line in octopi:
        for octopus in line:
            octopus.has_flashed = False
            octopus.value += 1

    # The, any octopus with an energy level greater than 9 flashes.
        # This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
        # If this causes an octopus to have an energy level great than 9, it also flashes.
        # This process continues as long as new octopuses keep having their energy level increased beyond 9.
            # An octopus can only flash at most once per step.
    
    process = True
    while process:
        process = False
        octopi_temp = [[Octopus(0) for i in line] for line in octopi]   
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                
                is_left = x != 0
                is_right = x != len(octopi[y]) - 1
                is_up = y != 0
                is_down = y != len(octopi) - 1
                
                if (octopi[y][x].value > 9) and (not octopi[y][x].has_flashed):
                    process = True
                    # check left
                    if is_left:
                        octopi_temp[y][x-1].value += 1
                            
                    # check right
                    if is_right:
                        octopi_temp[y][x+1].value += 1
                            
                    # check up
                    if is_up:
                        octopi_temp[y-1][x].value += 1
                            
                    # check down
                    if is_down:
                        octopi_temp[y+1][x].value += 1
                            
                    # check left up
                    if is_left and is_up:
                        octopi_temp[y-1][x-1].value += 1
                            
                    # check left down
                    if is_left and is_down:
                        octopi_temp[y+1][x-1].value += 1
                    
                    # check right up
                    if is_right and is_up:
                        octopi_temp[y-1][x+1].value += 1
                
                    # check right down
                    if is_right and is_down:
                        octopi_temp[y+1][x+1].value += 1
                        
                    octopi[y][x].has_flashed = True
                    
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                octopi[y][x].value += octopi_temp[y][x].value
            
            
    # Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            if octopi[y][x].value > 9:
                octopi[y][x].value = 0
                total_flashes += 1
               
    oprint(i)
    
print(total_flashes)

#%% PART 2 CODE

class Octopus:   
    
    def __init__(self, i):
        self.value = int(i)
        self.has_flashed = False

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value) + ',' + str(int(self.has_flashed))
        

octopi = [[Octopus(s) for s in line] for line in my_input]

def oprint(i=0):
    print(i)
    for line in octopi:
        print([str(o) for o in line])

sync_flash_bool = False
sync_flash_step = 0

steps = 100
# oprint()
step = 0
while(not sync_flash_bool):
    
    step += 1
        
    # First, the energy level of each octoups increases by 1
    
    for line in octopi:
        for octopus in line:
            octopus.has_flashed = False
            octopus.value += 1

    # The, any octopus with an energy level greater than 9 flashes.
        # This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
        # If this causes an octopus to have an energy level great than 9, it also flashes.
        # This process continues as long as new octopuses keep having their energy level increased beyond 9.
            # An octopus can only flash at most once per step.
    
    process = True
    while process:
        process = False
        octopi_temp = [[Octopus(0) for i in line] for line in octopi]   
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                
                is_left = x != 0
                is_right = x != len(octopi[y]) - 1
                is_up = y != 0
                is_down = y != len(octopi) - 1
                
                if (octopi[y][x].value > 9) and (not octopi[y][x].has_flashed):
                    process = True
                    # check left
                    if is_left:
                        octopi_temp[y][x-1].value += 1
                            
                    # check right
                    if is_right:
                        octopi_temp[y][x+1].value += 1
                            
                    # check up
                    if is_up:
                        octopi_temp[y-1][x].value += 1
                            
                    # check down
                    if is_down:
                        octopi_temp[y+1][x].value += 1
                            
                    # check left up
                    if is_left and is_up:
                        octopi_temp[y-1][x-1].value += 1
                            
                    # check left down
                    if is_left and is_down:
                        octopi_temp[y+1][x-1].value += 1
                    
                    # check right up
                    if is_right and is_up:
                        octopi_temp[y-1][x+1].value += 1
                
                    # check right down
                    if is_right and is_down:
                        octopi_temp[y+1][x+1].value += 1
                        
                    octopi[y][x].has_flashed = True
                    
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                octopi[y][x].value += octopi_temp[y][x].value
            
            
    # Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            if octopi[y][x].value > 9:
                octopi[y][x].value = 0
               
    # oprint(step)
    
    sync_flash_bool = True
    for line in octopi:
        for octopus in line:
            if not octopus.has_flashed:
                sync_flash_bool = False
                
    if sync_flash_bool:
        sync_flash_step = step
    
print(sync_flash_step)
