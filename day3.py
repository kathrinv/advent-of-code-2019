from typing import List

def load_day3_input(filename: str) -> List[str]:
    """
    Loads the input representing the wire
    directions
    
    Args:
        filename: The name of the file with
                  the inputs for Day 3. It
                  should be saved down to the
                  same directory.

    Returns:
        A list of strings representing the
        directions of the wires
    """
    with open('input3.txt') as f:
        lines = f.read().splitlines()
        wire1 = lines[0].split(',')
        wire2 = lines[1].split(',')
    return wire1, wire2

wire1, wire2 = load_day3_input('input3.txt')

def get_all_wire_locations(directions: List[str]) -> List[tuple]:
    """
    Translates all the wire directions into
    locations on a Cartesian plane. Uses
    helper function one_step to
    determine locations.
    
    Args:
        directions: List of strings representing
        the directions of the wires

    Returns:
        A list of tuples representing
        the locations of the wires
    """
    wire_locations = [(0,0)]
    for direction in directions:
        current_location = wire_locations[-1]
        wire_locations += one_step(current_location, direction)
    return wire_locations

def one_step(current_location: tuple, direction: str) -> List[tuple]:
    """
    Helper function for get_all_wire_locations()
    
    Args:
        direction: A string representing a
        single direction (up, left, right,
        or down) and a number of steps in
        said direction

    Returns:
        A list of tuples representing
        the locations of the wire
    """
    locations = []
    if direction[0] == 'U':
        for i in range(1, int(direction[1:])+1):
            next_location = (current_location[0],current_location[1]+1)
            locations.append(next_location)
            current_location = next_location
    elif direction[0] == 'D':
        for i in range(1, int(direction[1:])+1):
            next_location = (current_location[0],current_location[1]-1)
            locations.append(next_location)
            current_location = next_location
    elif direction[0] == 'L':
        for i in range(1, int(direction[1:])+1):
            next_location = (current_location[0]-1,current_location[1])
            locations.append(next_location)
            current_location = next_location
    else:
        for i in range(1, int(direction[1:])+1):
            next_location = (current_location[0]+1,current_location[1])
            locations.append(next_location)
            current_location = next_location
    return locations


def get_intersections(wire1_locs: List[tuple], wire2_locs: List[tuple]) -> List[tuple]:
    """
    Finds the intersection (the cross points)
    between wire1 and wire2
    
    Args:
        wire1_locs: A list of tuples representing
        the locations of the first wire
        wire2_locs: A list of tuples representing
        the locations of the second wire

    Returns:
        A list of tuples representing
        the intersection points of the wires
    """
    cross_points = []
    wire1_locs_set = set(wire1_locs)
    wire2_locs_set = set(wire2_locs)
    for loc in wire1_locs_set:
        if loc in wire2_locs_set:
            cross_points.append(loc)
    return cross_points

def get_shortest_distance(intersections: List[tuple]) -> int:
    """
    Finds the intersection with the
    shortest distance from the source point
    
    Args:
        intersections: A list of tuples
        of the wire cross points

    Returns:
        The manhattan disance of the
        cross point the shortest distance
        away from the source point of 
        the wires (0,0)
    """
    distances = []
    for intersection in intersections:
        distance = abs(intersection[0]) + abs(intersection[1])
        if distance != 0:
            distances.append(distance)
    return min(distances)

def get_shortest_steps(intersections: List[tuple], wire1_locs: List[tuple], wire2_locs: List[tuple]) -> int:
    num_steps = []
    for intersection in intersections:
        if intersection == (0,0):
            continue
        else:
            wire1_steps = wire1_locs.index(intersection)
            wire2_steps = wire2_locs.index(intersection)
            num_steps.append(wire1_steps + wire2_steps)
    return min(num_steps)

def day3(part2: bool = False, input_filename: str = 'input3.txt', wire1 = None, wire2 = None) -> int:
    """
    Returns the value in index 0 for part 1.
    
    For part 2, returns noun * 100 + verb
    (noun & verb being two integers that 
    replace indexes 1 and 2 of the 
    original intcode sequence) solution
    based on the supplied 'target' value
    for index 0
    
    Args:
        part2: Boolean indicating if solving
               for part 2
        input_filename: Expected input filename
        wire1, wire2 = Lists of strings
               representing wire diections.
               Optional parameters used for
               testing.

    Returns:
        An integer representing the manhattan
        distance of the closest intersection of
        two wires from the central port
    
    """
    if (not wire1) or (not wire2):
        wire1, wire2 = load_day3_input(input_filename)
    wire1_locs = get_all_wire_locations(wire1)
    wire2_locs = get_all_wire_locations(wire2)
    intersections = get_intersections(wire1_locs, wire2_locs)
    if not part2:
        min_distance = get_shortest_distance(intersections)
    else:
        min_distance = get_shortest_steps(intersections, wire1_locs, wire2_locs)
    return min_distance

# Day 3 Part 1 Testing - Manhattan Distance calculation
wire1_sample1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
wire2_sample1 = ['U62','R66','U55','R34','D71','R55','D58','R83']
assert day3(wire1 = wire1_sample1, wire2 = wire2_sample1) == 159, "Calculation of minimum distance of wire intersections from source is incorrect"

wire1_sample2 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
wire2_sample2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
assert day3(wire1 = wire1_sample2, wire2 = wire2_sample2) == 135, "Calculation of minimum distance of wire intersections from source is incorrect"

answer_part1 = day3()
answer_part2 = day3(part2=True)

print(f'The result to part 1 is: {answer_part1}')
print(f'The result to part 2 is: {answer_part2}')