# Task 1
"""
Write the method that return the number of threads currently in execution.
Also prepare the method that
will be executed with threads and run during the first method counting.
"""


import time
from threading import Thread, activeCount
import random


def func1():
    time.sleep(random.randint(1, 4))


def create_method():
    print(f'{activeCount()} is an active threads')


thread_1 = Thread(target=func1)
thread_2 = Thread(target=func1)

start = time.time()

thread_1.start()
thread_2.start()

create_method()

thread_1.join()
thread_2.join()

