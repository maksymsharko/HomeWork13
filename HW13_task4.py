# Task 4
"""
Divide the work between 2 methods: print_cube that returns the cube of number
and print_square that returns the square of number. These two methods
should be executed by using 2 different processes.
"""
from concurrent.futures import ProcessPoolExecutor
import time
import os
import random
from multiprocessing import Pool, Process


def print_cube(num1):
    id_name = os.getpid()
    start = time.time()
    print(f'Process: {id_name}')
    return print(f"The {num1} is elevated to the cube is equal to {num1} = {num1 ** 3} and this process continued "
                 f"{time.time() - start}")


def print_square(num2):
    id_name2 = os.getpid()
    start = time.time()
    print(f"Process: {id_name2}")
    return print(f"The {num2} is elevated to square is equal to {num2} = {num2 ** 2} and this process continued "
                 f"{time.time() - start}")


start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(print_cube, random.randint(1, 9))
    pool.submit(print_square, random.randint(1, 9))


print(f"Total time: {time.time() - start} ")
