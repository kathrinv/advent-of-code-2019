import pprint as pp
from typing import List

def load_day8_input(filename: str) -> str:
    """
    Loads the input representing the 
    image transmitted
    
    Args:
        filename: The name of the file with
                  the inputs for Day 8. It
                  should be saved down to the
                  same directory.

    Returns:
        A string of digits representing layers 
        in a 25 x 6 pixel image
    """
    image = ""
    with open(filename) as f:
        for line in f:
            image += line.replace('\n', '')
    return image


def split_into_layers(image: str) -> List[int]:
    """
    Takes the initial transmission
    and splits the string into 
    image layers.
    
    Args:
        image: A string of digits representing 
               layers in a 25 x 6 pixel image

    Returns:
        A list of layers, with each layer
        a list of int
    """
    
    layers = []
    for i in range(0, len(image), 25*6):
        start = i
        end = i + 25*6
        layers.append([int(char) for char in image[start:end]])
    return layers


def find_layer_with_least_zeros(layers: List[int]) -> List[int]:
    """
    Finds the layer with the least
    amount of zeros.
    
    Args:
         layers: A list of layers, with each layer
                 a list of int representing the color
                 of each pixel
    
    Returns:
        The pixel values of the layer with least zeros
        
    """
    least_zeros = None
    layer_index = None
    for idx, layer in enumerate(layers):
        num_zeros = sum([1 for num in layer if num == 0])
        if not least_zeros or num_zeros < least_zeros:
            least_zeros = num_zeros
            layer_index = idx
    return layers[layer_index]



def num_ones_times_num_twos(layer: List[int]) -> int:
    """
    Returns the number of ones
    times the numbers of twos
    in a layer.
    
        
    Args:
         layer: Pixel values of an image layer
    
    Returns:
        The number of 1 digits multiplied
        by the number of 2 digits in an
        image layer
        
    """
    num_ones = sum([1 for num in layer if num == 1])
    num_twos = sum([1 for num in layer if num == 2])
    return num_ones * num_twos


def decode_image(layers: List[int]) -> List[int]:
    """
    Prints out decoded image
    based on topmost visible pixel
    value.
    
    Args:
        layers: A list of layers, with each layer
                 a list of int representing the 
                 color of each pixel
    
    Returns:
        A formatted image showing a
        message
    
    """
    image = []
    for i in range(len(layers[0])):
        for j in range(len(layers)):
            if layers[j][i] == 0:
                image.append(' ')
                break
            elif layers[j][i] == 1:
                image.append('X')
                break
            else:
                continue # pixel is transparent
    formatted_image = []
    for k in range(0, 150, 25):
        
        formatted_image.append(''.join(image[k:k+25]))
    return formatted_image


def day8(filename: str = 'input8.txt', part2: bool = False):
    """
    Confirms correct image transmission
    by returning the number of 1 digits
    multiplied by the number of 2 digits
    in the image layer with the least
    amount of zeros.
    
    Change arguement 'part2' to True
    if image transmission was correct
    to decode the image.
    """
    image = load_day8_input(filename)
    layers = split_into_layers(image)
    if not part2:
        layer_with_least_zeros = find_layer_with_least_zeros(layers)
        result = num_ones_times_num_twos(layer_with_least_zeros)
        return result
    else:
        return decode_image(layers)


answer_part1 = day8()
answer_part2 = day8(part2=True)

print(f'The result to part 1 is: {answer_part1}')
print(f'The result to part 2 is:')
pp.pprint(answer_part2)
