from typing import List

def check_password_eligibility(i: int, part2: bool=False) -> bool:
    
    """
    Returns a boolean whether or not
    the password is eligible based on the criteria
    
    Args:
        i: 6-digit password in integer format
        part2: Boolean indicator of whether this is
            eligible password logic for part 1 
            or part 2

    Returns:
        Boolean value indicating if the password is
        eligible
    """
    
    i_str = str(i)
    length = len(i_str)
    # Criteria 1: Digits never decrease
    criteria1 = True 
    # Criteria 2: There are at least 2 adjacent digits that are the same
    criteria2 = [] 
    
    if not part2:
        # Iterating through the digits in the password to check the 2 criteria
        for j in range(0, 5):
            if int(i_str[j+1]) < int(i_str[j]):
                criteria1 = False
                break
            if int(i_str[j+1]) == int(i_str[j]):
                criteria2.append(True)
            else:
                criteria2.append(False)
    
    if part2:
        # Iterating through the digits in the password to check the 2 criteria
        for j in range(0, 5):
            if int(i_str[j+1]) < int(i_str[j]):
                criteria1 = False
                break
            if j == 0: # comparing first 2 digits
                if int(i_str[j+1]) == int(i_str[j]) and int(i_str[j+1]) != int(i_str[j+2]):
                    criteria2.append(True)
            elif j != 4: # comparings digits in the middle (all indices other than 0 and 5)
                if int(i_str[j+1]) == int(i_str[j]) and int(i_str[j+1]) != int(i_str[j+2]) and int(i_str[j]) != int(i_str[j-1]):
                    criteria2.append(True)
            else: # j == 4 - comparing last 2 digits
                if int(i_str[j+1]) == int(i_str[j]) and int(i_str[j]) != int(i_str[j-1]):
                    criteria2.append(True)
                
    # Two criteria must be satisfied for the password to be eligible
    if criteria1 and any(criteria2):
        return True
    else:
        return False
    
    
def day4(part2: bool = False, start: int = 402328, end: int = 864247):
    """
    """
    eligible_passwords = []
    
    #checking each number in the password range
    for i in range(start, end+1): 
        password_eligibility = check_password_eligibility(i, part2)
        if password_eligibility:
            eligible_passwords.append(i)

    return len(eligible_passwords)

# Day 4 Part 1 Testing - Password eligibility for Part 1
assert check_password_eligibility(111111) == True, "Password eligibility logic is incorrect for 111111 for part 1"
assert check_password_eligibility(223450) == False, "Password eligibility logic is incorrect for 223450 for part 1"
assert check_password_eligibility(123789) == False, "Password eligibility logic is incorrect for 123789 for part 1"


assert check_password_eligibility(112233, part2 = True) == True, "Password eligibility logic is incorrect for 112233 for part 2"
assert check_password_eligibility(123444, part2 = True) == False, "Password eligibility logic is incorrect for 123444 for part 2"
assert check_password_eligibility(111122, part2 = True) == True, "Password eligibility logic is incorrect for 111122 for part 2"

answer_part1 = day4()
answer_part2 = day4(part2=True)

print(f'The result to part 1 is: {answer_part1}')
print(f'The result to part 2 is: {answer_part2}')