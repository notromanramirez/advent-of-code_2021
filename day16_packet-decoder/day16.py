# Roman Ramirez, rr8rk@virginia.edu
# Advent of Code 2021, Day 16: Packet Decoder

#%% LONG INPUT
my_input = []
with open('input.txt', 'r') as f:
    for line in f:
        my_input.append(line.strip('\n'))

#%% EXAMPLE INPUT
my_input = [
    'A0016C880162017C3686B18A3D4780',
    '11101110000000001101010000001100100000100011000001100000',
    '00111000000000000110111101000101001010010001001000000000',
    'D2FE28'
    ]

#%% PART 1 CODE

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }

def bin_to_hex(n): #input is any string
    rets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return rets[int(n, 2)]

# 3-bit packet version
# 3-bit type ID

# if type ID == 4
    # 5-bit encoding for a single binary number
        # 1-bit to signal last number or not
        #4-bits to encode signal

# if type ID == 6
    # the packet is an operator
    # 1-bit encoding for length type ID
    # if length type ID == 0
        # 15-bit number that represents the total length in bits of sub-packets in this packet
    
    # if length type ID == 1
        # 11-bit number that represents the number of sub-packets immediately contained by this packet
        
def bin_to_string(s):
    bs = ''
    for char in s:
        bs += hex_to_bin.get(char)
    return bs

binary_string = bin_to_string(my_input[0])
# binary_string  = my_input[0]

def decode(bs):
    
    idx = 0
    
    retVal = ''
    
    # check version
    version_total = int(bs[idx:idx+3], 2)
    idx += 3
    
    # check type-id
    type_id = bs[idx:idx+3]
    idx += 3
    
    #if type ID == 4
    if type_id == '100':
        
        # 1-bit to signal last number or not
        is_not_last = True
        temp = ''
        while is_not_last:
            is_not_last = bool(int(bs[idx]))
            idx += 1
            
            temp += bs[idx:idx+4]
            idx += 4
            
        retVal = int(temp, 2)
        
    # operator packet
    else:
        length_type_id = bs[idx]
        idx += 1

        if length_type_id == '0':
            packet_length = int(bs[idx:idx+15], 2)
            idx += 15
            
            current_length = 0
            while current_length < packet_length:
            
                subversion, subRetVal, subidx = decode(bs[idx:])
                current_length += subidx
                idx += subidx
                version_total += subversion
            
        if length_type_id == '1':
            num_subpackets = int(bs[idx:idx+11], 2)
            idx += 11
        
            for _ in range(num_subpackets):
                subversion, subRetVal, subidx = decode(bs[idx:])
                idx += subidx
                version_total += subversion
                
        
    
            
    return version_total, retVal, idx

        
print(decode(binary_string)[0])

#%% PART 2 CODE

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }

def bin_to_hex(n): #input is any string
    rets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return rets[int(n, 2)]
        
def bin_to_string(s):
    bs = ''
    for char in s:
        bs += hex_to_bin.get(char)
    return bs

binary_string = bin_to_string(my_input[0])
# binary_string  = my_input[0]

def decode(bs):
    
    idx = 0
    
    retVal = ''
    
    # check version
    version_total = int(bs[idx:idx+3], 2)
    idx += 3
    
    # check type-id
    type_id = bs[idx:idx+3]
    idx += 3
    
    #if type ID == 4
    if type_id == '100':
        
        # 1-bit to signal last number or not
        is_not_last = True
        temp = ''
        while is_not_last:
            is_not_last = bool(int(bs[idx]))
            idx += 1
            
            temp += bs[idx:idx+4]
            idx += 4
            
        retVal = int(temp, 2)
        
    # operator packet
    else:
        
        length_type_id = bs[idx]
        idx += 1
        
        subRetVals = []

        if length_type_id == '0':
            packet_length = int(bs[idx:idx+15], 2)
            idx += 15
            
            current_length = 0
            while current_length < packet_length:
            
                subversion, subRetVal, subidx = decode(bs[idx:])
                current_length += subidx
                idx += subidx
                version_total += subversion
                subRetVals.append(subRetVal)
            
        elif length_type_id == '1':
            num_subpackets = int(bs[idx:idx+11], 2)
            idx += 11
        
            for _ in range(num_subpackets):
                subversion, subRetVal, subidx = decode(bs[idx:])
                idx += subidx
                version_total += subversion
                subRetVals.append(subRetVal)
                
        if type_id == '000':
            retVal = sum(subRetVals)
        elif type_id == '001':
            retVal = 1
            for x in subRetVals:
                retVal *= x
        elif type_id == '010':
            retVal = min(subRetVals)
        elif type_id == '011':
            retVal = max(subRetVals)
        elif type_id == '101':
            retVal = int(subRetVals[0] > subRetVals[1])
        elif type_id == '110':
            retVal = int(subRetVals[0] < subRetVals[1])
        elif type_id == '111':
            retVal = int(subRetVals[0] == subRetVals[1])
                

    return version_total, retVal, idx

        
print(decode(binary_string)[1])