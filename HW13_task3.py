# Task 3
"""
Use Pool.apply() to get the row wise common items in list_a and list_b.
list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
"""
from multiprocessing import Pool

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

common_items_ = []


def common_items(a, b):
    a1 = set(a)
    b1 = set(b)
    return list(a1.intersection(b1))


pool = Pool()
if __name__ == "__main__":
    for x in range(len(list_a)):
        common_items_.append(pool.apply(common_items, [list_a[x], list_b[x]]))
    print(common_items_)
