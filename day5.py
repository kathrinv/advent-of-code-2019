from typing import List

def load_day5_input(filename: str) -> List[int]:
    """
    Loads the input representing the incode
    program
    
    Args:
        filename: The name of the file with
                  the inputs for Day 5. It
                  should be saved down to the
                  same directory.

    Returns:
        A list of integers
    """
    intcode_lst = []
    with open(filename) as f:
        for line in f:
            intcode_lst += line.split(',')
    intcode_lst[-1] = intcode_lst[-1].replace('\n', '')
    intcode_lst_int = [int(i) for i in intcode_lst]
    return intcode_lst_int
            

def replace_digits(num1: int, num2: int, intcode_lst: List['int']) -> List['int']:
    """
    Replaces the 1st and 2nd index positions
    in the intcode list
    
    Args:
        num1: Integer replacing index 1 in intcode_lst 
        num2: Integer replacing index 2 in intcode_lst 
        intcode_lst: Intcode program

    Returns:
        Modified Intcode program
    """
    intcode_lst[1] = num1
    intcode_lst[2] = num2
    return intcode_lst

def opcode_program(intcode_lst: List['int'], input_value = 1, parameter = 0) -> int:
    """
    Conducts the intcode program
    
    Args:
        intcode_lst: Intcode program

    Returns:
        Integer value in position 0
        of modified intcode list
    """
    current_pos = 0
#     lst_len = len(intcode_lst)
    while True:
        if intcode_lst[current_pos] == 99:
            break
        else:
            opcode = str(intcode_lst[current_pos])[-1:]
            print(opcode)
            
            if opcode == '3':
                intcode_lst[input_value] = intcode_lst[current_pos + 1]
                current_pos += 2
#                 print(intcode_lst[current_pos])
            elif opcode == '4':
                if len(str(intcode_lst[current_pos])) == 1:
                    input_value = intcode_lst[intcode_lst[current_pos + 1]]
                else:
                    input_value = intcode_lst[current_pos + 1]
                current_pos += 2
#                 print(intcode_lst[current_pos])
            else:
                end = current_pos + 4
                new_value, pos_to_replace = opcode_calc(intcode_lst, intcode_lst[current_pos:end])
                intcode_lst[pos_to_replace] = new_value
                current_pos += 4
#                 print(intcode_lst[current_pos])
    return intcode_lst[0]

def find_verb_noun(input_filename: str = 'input2.txt', target: int = 19690720) -> int:
    """
    Iterates through 0->100 for index
    positions 1 and 2 to find appropriate
    starters (noun, verb) to calculate 
    the target.
    
    Args:
        input_filename: Expected input filename
        target: Expected value for index 0

    Returns:
        Either noun * 100 + verb or
        'no result found' if target
        condition cannot be met
    
    """
    for i in range(0, 100):
        for j in range(0, 100):
            intcode_lst = load_day2_input(input_filename)
            temp_intcode_lst = replace_digits(i, j, intcode_lst)
            result = opcode_calc(temp_intcode_lst)
            if result == target:
                return 100 * i + j
    return "no result found"

# def day5(part5: bool = False, input_filename: str = 'input5.txt', num1 = 12, num2 = 2, target=19690720) -> int:
#     """
#     Returns the value in index 0 for part 1.
    
#     For part 2, returns noun * 100 + verb
#     (noun & verb being two integers that 
#     replace indexes 1 and 2 of the 
#     original intcode sequence) solution
#     based on the supplied 'target' value
#     for index 0
    
#     Args:
#         part2: Boolean indicating if solving
#                for part 2
#         input_filename: Expected input filename
        
#         For Part 1:
#         num1: Integer replacing index 1 in intcode_lst 
#         num2: Integer replacing index 2 in intcode_lst 
        
#         Fort Part 2:
#         target: Expected value for index 0

#     Returns:
#         Either value in position 0 for Part 1
#         or noun * 100 + verb for Part 2
    
#     """
#     if not part2:
#         intcode_lst = load_day2_input(input_filename)
#         temp_intcode_lst = replace_digits(num1, num2, intcode_lst)
#         position0 = opcode_calc(temp_intcode_lst)
#         return position0
#     else:
#         return find_verb_noun(input_filename, target=target)
        

# # Day 2 Part 1 Testing - opcode calculation logic
# assert opcode_calc([1,9,10,3,2,3,11,0,99,30,40,50]) == 3500, "calculation using opcodes is incorrect"
# assert opcode_calc([2,3,0,3,99]) == 2, "calculation using opcodes is incorrect"
# assert opcode_calc([2,4,4,5,99,0]) == 2, "calculation using opcodes is incorrect"
# assert opcode_calc([1,1,1,4,99,5,6,0,99]) == 30, "calculation using opcodes is incorrect"
# assert opcode_calc([1,0,0,0,99]) == 2, "calculation using opcodes is incorrect"

# # Day 2 Part 2 Testing - finding the noun and verb diven a target value for position 0
# assert find_verb_noun(target=3101878) == 1202, "calculation to find noun and verb is incorrect"

# answer_part1 = day5()
# answer_part2 = day5(part2=True)

# print(f'The result to part 1 is: {answer_part1}')
# print(f'The result to part 2 is: {answer_part2}')