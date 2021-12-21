# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 20: Trench Map

#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
    '',
    '#..#.',
    '#....',
    '##..#',
    '..#..',
    '..###'
    ]

#%% PART 1 AND 2 CODE

def im_to_bin(s):
    accum = ''
    for char in s:
        accum += '1' if (char == '#') else '0'
    return accum

iea = my_input[0]

# from 5 by 5
input_image = my_input[2:]
output_image = input_image
   
# input is (x + 2) by (x + 2), output is (x) by (x)
def covolution(image, x, y):
    accum = ''
    for h in range(y-1, y+2):
        accum += image[h][x-1:x+2]
        
    index = int(im_to_bin(accum), 2)
    return iea[index]

def image_convolution(image):
    # expecting (x by 2) x (x by 2)
    output_image = list()
    
    for y in range(1, len(image) - 1):
        line = ''
        for x in range(1, len(image[y]) - 1):
            line += covolution(image, x, y)
        output_image.append(line)
        
    return output_image
    
pad_size = 2
iterations = 50
for i in range(iterations):
    ## zero-padding
    pc = '#' if i % 2 and iea[0] == '#' else '.'
    # from (x) by (x) to (x + 4) by (x)
    side_padded = [pc * pad_size + line + pc * pad_size for line in output_image]
    # from (x + 4) by (x) to (x + 4) by (x + 4)
    zero_padded = [pc * len(side_padded[0])] * pad_size + side_padded + [pc * len(side_padded[0])] * pad_size
    
    ## convolution
    output_image = image_convolution(zero_padded)
   
    ones = 0
    for y, line in enumerate(output_image):
        for x, char in enumerate(line):
            if char == '#':
                ones += 1
                
    print(i+1, ones)
    # for line in output_image:
    #     print(line)
