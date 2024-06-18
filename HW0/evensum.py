"""
file: cubes.py
description: we need to print the sum of even nums
             out of the given numbers.
language: python3
author: Dhruv Dave, dd7540@rit.edu
        Mariam Abidi, ma6267@rit.edu

"""

def cubes():
    # we take the input form the user
    n = input()
    sum = 0
    for i in range(int(n)):
        num = int(input())
        if num % 2 == 0:
            sum += num
    print(sum)

if __name__ == '__main__':
    cubes()
