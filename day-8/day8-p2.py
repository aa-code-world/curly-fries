""" 
 2023 AoC Day 8 Part 2
 Annies Abduljaffar
"""

import math 
navigation_steps = dict()

def main():
    lines = open("input.txt").readlines()
    pattern = lines[0].strip()

    for i in range(2, len(lines)):
        start = lines[i].split('=')[0].strip()
        left = lines[i].split('=')[1].split(',')[0].split('(')[1].strip()
        right = lines[i].split('=')[1].split(',')[1].split(')')[0].strip()
        navigation_steps[start] = [left, right]


    steps_list = [] 
    for dest in get_starting_points():
        index = 0
        steps = 0 
        while (dest[-1] != 'Z'):
            if (pattern[index] == 'L'):
                dest = navigation_steps[dest][0]
            else:
                dest = navigation_steps[dest][1]
            if (index + 1 == len(pattern)):
                index  = 0
            else:
                index = index + 1
            steps = steps + 1
        
        steps_list.append(steps)

    print(steps_list)
    #then find lcm

def get_starting_points():
    temp = []
    for key in navigation_steps.keys():
        if key[-1] == 'A':
            temp.append(key)
    return temp


if __name__ == "__main__":
    main()
    