# This is a sample Python script.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    file = open('test.txt')
    count = 0
    for line in file:
        count += 1

    inp = file.read()
    print('Line count:', count)
    data = dict()

    data["gg"] = 4

    for (k, v) in data.items():
        print(k, v)

    d = dict()
    d['quincy'] = 1
    d['beau'] = 5
    d['kris'] = 9
    for (k, i) in d.items():
        print(k, i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    a = np.array([[1, 2, 3], [1, 2, 5]])
    print("Metric " + str(a.ndim))

    # Type of element
    print(a.dtype)

    # Size, Shape
    print(a.size)
    print(a.shape)

    a = a.reshape(3, 2)
    print(a)

    x = [3, 5]
    y = [7, 9]

    r = np.linspace(0.0, 1)

    plt.plot(x, y)

    plt.scatter(x, y)
    plt.show()

    d = {'a': 10, 'b': 1, 'c': 2}
    d.items()
    sorted(d.items())

    lst = []
    for key, val in d.items():
        newtup = (val, key)
        lst.append(newtup)

    lst = sorted(lst, reverse=True)

    fhand = open('romeo.txt')
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    lst = list()
    for val, key in lst[: 10]:
        print(key, val)

    c = {'a': 10, 'b': 1, 'c': 22}
    sorted([(v, k) for k, v in c.items()])


# def solveNQueens(self, n: int) -> List[List[str]]:


def regexStr():
    hand = open('mbox-short.txt')
    for line in hand:
        line = line.rstrip()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def sort(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    return a
