""" 
 2023 AoC Day 4 Part 1
 Annies Abduljaffar
"""
import re 

def main():
    line_number = 0
    winners =  matrix = [['0' for _ in range(10)] for _ in range(193)]
    draws =  matrix = [['0' for _ in range(25)] for _ in range(193)]

    for line in open("input/input.txt"):
        line=line.split(":")[1].strip()
        j = 0
        for test in re.split(' +', line.split('|')[0].strip()):
            winners[line_number][j] = test
            j = j +1
        j=0
        for test in re.split(' +', line.split('|')[1].strip()):
            draws[line_number][j] = test
            j = j +1
        line_number = line_number +1

    total = 0
    for card in range(193):
        card_value = 0
        for winner in range(10):
            for draw in range(25):
                if (winners[card][winner] == draws[card][draw]) :
                    if(card_value ==0):
                        card_value = 1
                    else:
                        card_value = card_value*2
        total = total + card_value
    print(total)

if __name__ == "__main__":
    main()