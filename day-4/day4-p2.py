""" 
 2023 AoC Day 4 Part 2
 Annies Abduljaffar
"""
import re 

def main():
    n_cards = 193
    n_winners = 10
    n_draws = 25

    line_number = 0
    winners =  matrix = [['0' for _ in range(n_winners)] for _ in range(n_cards)]
    draws =  matrix = [['0' for _ in range(n_draws)] for _ in range(n_cards)]
    card_matches= dict()
    card_counts = dict()

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

    for card in range(n_cards):
        num_matches = 0
        for winner in range(n_winners):
            for draw in range(n_draws):
                if (winners[card][winner] == draws[card][draw]) :
                    num_matches = num_matches + 1 
        card_matches[card]=num_matches
        card_counts[card]=1

    for card in range(n_cards):
        card_value=card_matches[card]
        for num_cur_cards in range(card_counts[card]):
            i=card+1
            for it in range(card_value):
                if(i<n_cards):
                    card_counts[i] = int(card_counts[i]) + 1 
                i = i+1
        print(card_counts)

    total = 0
    for card in range(n_cards):
        total = total + card_counts[card]
        
    print(total)


if __name__ == "__main__":
    main()
