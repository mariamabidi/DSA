"""
file: cubes.py
description: we need to print perfect cubes
        till a given number.
language: python3
author: Dhruv Dave, dd7540@rit.edu
        Mariam Abidi, ma6267@rit.edu

"""

def cubes():
    # we take the input form the user
    n = input()
    cube = 0
    # we use a while loop to loop through all the possible cubes less than input.
    while cube * cube * cube <= int(n):
        print(cube * cube * cube)
        cube += 1


if __name__ == '__main__':
    cubes()
