from itertools import permutations
from tqdm import tqdm
from time import time
from math import factorial
import json

import sys

if sys.version_info[0] != 3:
    raise Exception("Requires python of version 3")

"""
Square list index pattern
[0][1][2]
[3][4][5]
[6][7][8]
"""

def square_validator(square):
    temp = [x**2 for x in square]
    return (temp[0]+temp[1]+temp[2]) == (temp[3]+temp[4]+temp[5]) == (temp[6]+temp[7]+temp[8]) == (temp[0]+temp[3]+temp[6]) == (temp[1]+temp[4]+temp[7]) == (temp[2]+temp[5]+temp[8]) == (temp[0]+temp[4]+temp[8]) == (temp[2]+temp[4]+temp[6])


def calculate_queue_length(highest_number):
    return factorial(highest_number) / factorial(highest_number-9)

def main(highest_number):
    queue = permutations(range(highest_number), 9)
    queue_length = calculate_queue_length(highest_number)
    true_squares = []

    start = time()

    for square in tqdm(queue, desc="Subsets", leave=False, total=queue_length, unit="subset"):
        if square_validator(square):
            true_squares.append(square)
    
    print(f"It took {round(time()-start, 2)} seconds, found {len(true_squares)} working squares. Went through {queue_length}")

    with open('result.json', 'w') as file:
        json.dump(true_squares, file)

if __name__ == '__main__':
    main(int(input("What is the highest number? ")))