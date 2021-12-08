# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code, Day 8: Seven Segment Search

#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
    ]

#%% PART 1 CODE

# only 1 uses 2 segments
# only 4 uses 4 segments
# only 7 uses 3 segments
# only 8 uses 7 segments

# 2 uses 5 segments
# 3 uses 5 segments
# 5 uses 5 segments

# 0 uses 6 segments
# 6 uses 6 segments
# 9 uses 6 segments

signal_patterns = []
output_values = []
for line in my_input:
    temp = line.split(' | ')
    signal_patterns.append(temp[0].split(' '))
    output_values.append(temp[1].split(' '))
    
total = 0
for output_line in output_values:
    for number in output_line:
        size = len(number)
        if ((size == 2) or (size == 3) or (size == 4) or (size == 7)):
            total += 1
            
print(total)

#%% PART 2 CODE

# only 1 uses 2 segments
# only 4 uses 4 segments
# only 7 uses 3 segments
# only 8 uses 7 segments

# 2 uses 5 segments
# 3 uses 5 segments
# 5 uses 5 segments

# 0 uses 6 segments
# 6 uses 6 segments
# 9 uses 6 segments

def sort(s):
    return "".join(sorted(s))

signal_patterns = []
output_values = []
for line in my_input:
    temp = line.split(' | ')
    signal_patterns.append([sort(s) for s in temp[0].split(' ')])
    output_values.append([sort(s) for s in temp[1].split(' ')])


# does s1 have s2?
def has(s1, s2):
    return all([s1.__contains__(s) for s in s2])
    

def decode(signal_pattern):
    
    string_to_num = {}
    num_to_string = {}
    
    for string in signal_pattern:
        # 1 uses 2 segments
        if len(string) == 2:
            string_to_num[string] = 1
            num_to_string[1] = string
        # 4 uses 4 segments
        elif len(string) == 4:
            string_to_num[string] = 4
            num_to_string[4] = string
        # 7 uses 3 segments
        elif len(string) == 3:
            string_to_num[string] = 7
            num_to_string[7] = string
        # 8 uses 6 segments
        elif len(string) == 7:
            string_to_num[string] = 8
            num_to_string[8] = string
                
    for string in signal_pattern:        
        # 0 uses 6 segments
        # 6 uses 6 segments
        # 9 uses 6 segments
        if len(string) == 6:
            # 6 does not have the shape of 7
            if (not has(string, num_to_string.get(7))):
                string_to_num[string] = 6
                num_to_string[6] = string
            else:
                # 9 has the shape of 4
                if has(string, num_to_string.get(4)):
                    string_to_num[string] = 9
                    num_to_string[9] = string
                # 0 does not have the shape of 4
                else:
                    string_to_num[string] = 0
                    num_to_string[0] = string
                    
    
            
    for string in signal_pattern:
        # 5 uses 5 segments
        if len(string) == 5:
            # 3 has the shape of 1
            if (has(string, num_to_string.get(1))):
                string_to_num[string] = 3
                num_to_string[3] = string
            else:
                # 6 has the shape of 5
                if has(num_to_string.get(6), string):
                    string_to_num[string] = 5
                    num_to_string[5] = string
                
                else:
                    string_to_num[string] = 2
                    num_to_string[2] = string
                
    # a mapping between 
    return string_to_num

def decipher(alg, output_value):
    s = ""
    for val in output_value:
        s += str(alg.get(val))
    return int(s)

total = 0
for i in zip(signal_patterns, output_values):
    line_alg = decode(i[0])
    # print(decode(i[0]))
    total += decipher(line_alg, i[1])

print(total)
