from typing import List, Set

def load_day6_input(filename: str) -> List[int]:
    """
    Loads the input representing the incode
    program
    
    Args:
        filename: The name of the file with
                  the inputs for Day 6. It
                  should be saved down to the
                  same directory.

    Returns:
        A set of tiples representing the 
        a direct orbit of two plants
    """
    all_orbits = []
    with open(filename) as f:
        for line in f:
            orbit = line.split(')')
            orbit[1] = orbit[1].replace('\n', '')
            all_orbits.append(tuple(orbit))
    return set(all_orbits)



# works but is slow due to recursive calculation
def count_orbits(all_orbits: Set[str]) -> int:
    """
    Counts the total of direct and indirect
    orbits for each of the planets in the map.
    Uses helper recursive function
    count_indirect_orbits()
    
    Args:
        all_orbits: A set of tuples representing 
        the a direct orbit of two plants

    Returns:
        Integer representing the number
        of direct and indirect orbits
        for all planets
    """
    orbit_count = 0
    all_orbits_set = set([orbit[1] for orbit in all_orbits])
    for orbit in all_orbits:
        orbit_count += 1 # adding direct orbit to the count
        # adding indirect orbits to the count
        orbit_count += count_indirect_orbits(all_orbits, all_orbits_set, orbit[0])
    return orbit_count

def count_indirect_orbits(all_orbits: Set[str], all_orbits_set: Set[str], planet: str) -> int:
    """
    Counts the total indirect orbits for 
    one planet. Recursive function.
    
    Args:
        all_orbits: A set of tuples representing 
        the a direct orbit of two plants
        
        all_orbits_set: A set of planets that
        directly orbit another planet
        
        planet: The planet for which we will count
        indirect orbits

    Returns:
        Integer representing the number
        of indirect orbits for one planet
    """
    
    # base case
    if planet not in all_orbits_set:
        return 0
    # recursive case
    else:
        next_planet = [orbit[0] for orbit in all_orbits if orbit[1] == planet]
        return 1 + count_indirect_orbits(all_orbits, all_orbits_set, next_planet[0])

def day6(filename: str = 'input6.txt', part2: bool = False):
    if not part2: 
        all_orbits = load_day6_input(filename)
        total_orbits = count_orbits(all_orbits)
    return total_orbits
        
    
    
example_orbit = [('COM','B'), ('B','C'), ('C','D'), ('D','E'), ('E','F'), ('B','G'), ('G','H'),
                 ('D','I'), ('E','J'), ('J','K'), ('K','L')]

assert count_orbits(example_orbit) == 42, "orbit count logic is incorrect"
answer_part1 = day6()
# answer_part2 = day2(part2=True)

print(f'The result to part 1 is: {answer_part1}')
# print(f'The result to part 2 is: {answer_part2}')
