from typing import List

def load_day1_input(filename: str) -> List[int]:
    """
    Loads the input representing the mass
    of various flight modules
    
    Args:
    filename: The name of the file with
              the inputs for Day 1. It
              should be saved down to the
              same directory.

    Returns:
        A list of integers
    """
    mass_lst = []
    with open(filename) as f:
        for line in f:
            mass_lst.append(int(line))
    return mass_lst


def get_total_fuel_requirements(mass_lst: List[int]) -> int:
    """
    Iterates through the list of masses,
    calls the function to calculate fuel,
    and returns the total fuel requirement.
    
    Args:
        mass_lst: List of masses (int)

    Returns:
        The total fuel requirement
    """
    total_fuel = 0
    for mass in mass_lst:
        fuel_requirement = get_fuel_requirements(mass)
        total_fuel += fuel_requirement
    return total_fuel

def get_fuel_requirements(mass: int) -> int:
    """
    Calculates the fuel requirement.
    
    Args:
        mass: An integer representing the mass
        of one module

    Returns:
        The fuel requirement for one module
    """
    return int(mass / 3) - 2


def get_total_fuel_requirements_part2(mass_lst: List[int]) -> int:
    """
    Iterates through the list of masses,
    calls the function to calculate fuel,
    and returns the total fuel requirement
    taking into account the mass of the
    added fuel.
    
    Args:
        mass_lst: List of masses (int)

    Returns:
        The total fuel requirement
    """
    total_fuel = 0
    for mass in mass_lst:
        while True:
            if get_fuel_requirements(mass) <= 0:
                break
            else:
                mass = get_fuel_requirements(mass)
                total_fuel += mass
    return total_fuel


def day1(part2: bool = False, input_filename='input.txt') -> int:
    """
    Returns the total fuel required.
    Change arguement 'part2' to True
    if calculating fuel requirement
    for part 2 of Day 1's challenege
    """
    mass_lst = load_day1_input(input_filename)
    if part2:
        total_fuel = get_total_fuel_requirements_part2(mass_lst)
    else:
        total_fuel = get_total_fuel_requirements(mass_lst)
    return total_fuel


# Day 1 Part 1 Testing - fuel requirement calculation logic
assert get_fuel_requirements(12) == 2, "calculation to get fuel requirements is incorrect"
assert get_fuel_requirements(14) == 2, "calculation to get fuel requirements is incorrect"
assert get_fuel_requirements(1969) == 654, "calculation to get fuel requirements is incorrect"
assert get_fuel_requirements(100756) == 33583, "calculation to get fuel requirements is incorrect"

# Day 1 Part 2 Testing - fuel requirement calculation logic given additional fuel mass
assert get_total_fuel_requirements_part2([14]) == 2, "calculation to get fuel requirements for part 2 is incorrect"
assert get_total_fuel_requirements_part2([1969]) == 966, "calculation to get fuel requirements for part 2 is incorrect"
assert get_total_fuel_requirements_part2([100756]) == 50346, "calculation to get fuel requirements for part 2 is incorrect"

answer_part1 = day1()
answer_part2 = day1(part2=True)

print(f'The result to part 1 is: {answer_part1}')
print(f'The result to part 2 is: {answer_part2}')











