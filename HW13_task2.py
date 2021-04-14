# Task 2
"""
Print current date by using 2 threads.
#1. Define a subclass using Thread class.
#2. Instantiate the subclass and trigger the thread.
"""
import random
from threading import Thread
import time
from datetime import datetime


class ClassTodayDate(Thread):

    def run(self):
        # self.is_not_used()
        today = datetime.date(datetime.now())
        print(f"Current date: {today}")
        time.sleep(random.randint(1, 3))

    # def is_not_used(self):
        # pass


def main():
    thread1 = ClassTodayDate()
    thread1.start()
    thread2 = ClassTodayDate()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()