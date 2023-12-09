""" 2023 AoC Day 9 Part 2 """
def main():
    total_of_predictions = 0
    for line in open("input.txt").readlines():
        seed_values = [int(i) for i in line.strip().split(' ')]
        total_of_predictions = total_of_predictions + get_prediction(seed_values)
    print(total_of_predictions)

def get_prediction(sequence):
    if all(num == 0 for num in sequence):
        return 0
    return sequence[0] - get_prediction(reduce(sequence))

def reduce(sequence):
    temp = []
    for i in range(1, len(sequence)) :
        temp.append(sequence[i] - sequence[i-1])
    return temp

if __name__ == "__main__":
    main()
    