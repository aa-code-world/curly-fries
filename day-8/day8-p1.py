""" 
 2023 AoC Day 8 Part 2
 Annies Abduljaffar
"""


def main():
    navigation_steps = dict()
    lines = open("input.txt").readlines()
    pattern = lines[0].strip()

    for i in range(2, len(lines)):
        start = lines[i].split('=')[0].strip()
        left = lines[i].split('=')[1].split(',')[0].split('(')[1].strip()
        right = lines[i].split('=')[1].split(',')[1].split(')')[0].strip()
        navigation_steps[start] = [left, right]

    total_steps = 0
    dest = 'AAA'
    index = 0
    while (not dest == 'ZZZ'):
        total_steps = total_steps + 1
        if (pattern[index] == 'L'):
            print(navigation_steps[dest][0])
            dest = navigation_steps[dest][0]
        else:
            print(navigation_steps[dest][1])
            dest = navigation_steps[dest][1]
        if (index + 1 == len(pattern)):
            index  = 0
        else:
            index = index + 1

    print(total_steps)

if __name__ == "__main__":
    main()
    