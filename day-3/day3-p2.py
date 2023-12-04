""" 
 2023 AoC Day 3 Part 2
"""
import re 

columns = 140
col_index = columns - 1

def main():
    matrix = parse()
    total = line_number = 0
    visited_items = dict()
    lines=open("input/input.txt").readlines()

    for line in lines:
        for match in re.finditer('\d+', line):
            number = match.group()
            x, y, result = check_surrounding(number, line_number, match.start(), matrix)
            if(result):
                pair, result = return_same_line_pair(x, y, matrix, lines)
                if (result and number != pair and not visited_items.get(str(x)+'-'+str(y))):
                    visited_items[str(x)+'-'+str(y)] = True
                    total = total + int(number)* int(pair)
                pair, result = return_next_line_pair(x, y, matrix, lines)
                if (result and number != pair and not visited_items.get(str(x)+'-'+str(y))):
                    visited_items[str(x)+'-'+str(y)] = True
                    total = total + int(number)* int(pair)
                pair, result = return_prev_line_pair(x, y, matrix, lines)
                if (result and number != pair and not visited_items.get(str(x)+'-'+str(y))):
                    visited_items[str(x)+'-'+str(y)] = True
                    total = total + int(number)* int(pair)
        line_number = line_number + 1
    print(total)

def parse():
    matrix = [['0' for _ in range(columns)] for _ in range(columns)]
    i = 0
    for line in open("input/input.txt"):
        for j in range(0,columns):
            matrix[i][j] = line[j]
        i = i + 1
    return matrix

def check_surrounding(number, i, index, matrix):
    has_symbol = False
    for j in range(index, index+len(str(number))):
        if (i-1 >= 0): 
            if (is_symbol(matrix[i-1][j])):
                return i-1, j, True  
        if (i+1 <= col_index): 
            if (is_symbol(matrix[i+1][j])):
                return i+1, j, True  
        if (j-1 >= 0): 
            if ( is_symbol(matrix[i][j-1])):
                return i, j-1, True  
        if (j+1 <= col_index): 
            if ( is_symbol(matrix[i][j+1])):
                return i, j+1, True  
        if (i-1 >= 0 and j-1 >= 0): 
            if ( is_symbol(matrix[i-1][j-1])):
                return i-1, j-1, True  
        if (i+1 <= col_index and j+1 <= col_index): 
            if ( is_symbol(matrix[i+1][j+1])):
                return i+1, j+1, True  
        if (i-1 >= 0 and j+1 <= col_index): 
            if ( is_symbol(matrix[i-1][j+1])):
                return i-1, j+1, True  
        if (i+1 <= col_index and j-1 >= 0): 
            if ( is_symbol(matrix[i+1][j-1])):
                return i+1, j-1, True  
    return 0,0, False


def return_same_line_pair(row, col, matrix,lines):
    line = lines[row]
    for match in re.finditer('\d+', line):
        number = match.group()
        x, y, result = check_surrounding(number, row, match.start(), matrix)
        if (x==row and y==col):
            return number, True
    return 0, False

def return_next_line_pair(row, col, matrix, lines):
    if(row+1 <= col_index):
        line = lines[row+1]
        for match in re.finditer('\d+', line):
            number = match.group()
            x, y, result = check_surrounding(number, row+1, match.start(), matrix)
            if (x==row and y==col):
                return number, True
        return 0, False

def return_prev_line_pair(row, col, matrix, lines):
    if(row-1 >= 0):
        line = lines[row-1]
        for match in re.finditer('\d+', line):
            number = match.group()
            x, y, result = check_surrounding(number, row-1, match.start(), matrix)
            if (x==row and y==col):
                return number, True
    return 0, False


def is_symbol(character):
    return character in ('*')

if __name__ == "__main__":
    main()
    