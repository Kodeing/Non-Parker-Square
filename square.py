from itertools import permutations
from tqdm import tqdm
from time import time
from math import factorial

"""
Square list index pattern
[0][1][2]
[3][4][5]
[6][7][8]
"""

def square_validator(square):
    temp = [x**2 for x in square]
    s1 = temp[0] + temp[1] + temp[2]
    s2 = temp[3] + temp[4] + temp[5]
    s3 = temp[6] + temp[7] + temp[8]
    s4 = temp[0] + temp[3] + temp[6]
    s5 = temp[1] + temp[4] + temp[7]
    s6 = temp[2] + temp[5] + temp[8]
    s7 = temp[0] + temp[4] + temp[8]
    s8 = temp[2] + temp[4] + temp[6]
    if s1 != s2: return False
    if s2 != s3: return False
    if s3 != s4: return False
    if s4 != s5: return False
    if s5 != s6: return False
    if s6 != s7: return False
    if s7 != s8: return False
    return True

def calculate_queue_length(highest_number):
    return factorial(highest_number) / factorial(highest_number-9)

def main():
    highest_number = 11
    queue = permutations(range(highest_number), 9)
    queue_length = calculate_queue_length(highest_number)
    true_squares = []

    start = time()

    for square in tqdm(queue, desc="Subsets", leave=False, total=queue_length, unit="subset"):
        if square_validator(square):
            true_squares.append(square)
    
    print(f"It took {round(time()-start, 2)} seconds, found {len(true_squares)} working squares. Went through {queue_length}")

    if len(true_squares) > 0:
        print(true_squares)

if __name__ == '__main__':
    main()