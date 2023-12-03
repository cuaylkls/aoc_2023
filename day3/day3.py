from typing import List


# loads all lines in the file into a list
def load_file_to_matrix(file_path: str) -> List[str]:
    ret: List[str] = []

    with open(file_path, 'r') as f:
        for line in f:
            ret.append(line.strip())

    return ret


# takes a character input, return true if
# the character is not a numeric digit or
# a . (period)
def is_symbol(cc: str) -> bool:
    return (not cc.isdigit()) and (cc != '.')


# processes digits in a number, the number is valid, return the integer value
# otherwise return 0
def process_number(digits: str, valid: bool) -> int:
    if valid:
        output_txt = f"\033[0;32;40m{digits}\033[0;0m"
        ret = int(digits)
    else:
        output_txt = f"{digits}"
        ret = 0

    print(output_txt, end='')

    return ret


# step 1) load the input file into a 2D matrix
path = 'input.txt'
matrix = load_file_to_matrix(path)

# step 2) step through the matrix one cell at a time

# get the length of each side of the matrix
x_len = len(matrix[0])
y_len = len(matrix)

# offsets to apply to co-ordinates for each cell surrounding the current cell
adjacent_offsets = [
    (0, -1),   # top
    (-1, -1),  # top left
    (-1, 0),   # left
    (-1, 1),   # bottom left
    (0, 1),    # bottom
    (1, 1),    # bottom right
    (1, 0),    # right
    (1, -1),   # top right
]

# variable to store the sum of valid numbers
valid_number_total = 0

# initilise a buffer to hold numeric digits as they are found
cur_number_c = ''

# inisilise a flag which indicates whether a number is valid
valid_number = False

# loop through each value in the matrix
for y in range(y_len):
    for x in range(y_len):
        # obtain the character to test
        c = matrix[y][x]

        # check if the character is a digit
        if c.isdigit():
            # add to the number buffer
            cur_number_c += c

            # step 3) where a number is found, look for a symbol in the surrounding co-ordinates; it the symbol is found
            # mark as valid. Only check if the number has not already been found to be valid
            if not valid_number:
                # check each of the surrounding cells
                for x_off, y_off in adjacent_offsets:
                    x_chk = x + x_off
                    y_chk = y + y_off

                    # check for invalid co-ordinates and skip if not valid
                    if (x_chk < 0) or (y_chk < 0) or (x_chk >= x_len) or (y_chk >= y_len):
                        continue

                    # if a symbol is found, mark as valid and stop checking
                    if is_symbol(matrix[y_chk][x_chk]):
                        valid_number = True
                        break
        else:
            # step 4) stop reading the number when a non numeric character is encountered
            if cur_number_c != '':
                # a non-numeric character immediately after a number indicates the end of
                # a string of number characters

                # add the number fo the total if it is valid and print the number
                valid_number_total += process_number(cur_number_c, valid_number)

                # reset the buffer and flag
                cur_number_c = ''
                valid_number = False

            # print the current character
            print(c, end='')

    else:
        # caters for number at the end of the line
        if cur_number_c != '':
            valid_number_total += process_number(cur_number_c, valid_number)

            cur_number_c = ''
            valid_number = False

        # print a new line as at end of line
        print('')


print(f"Part 1: {valid_number_total} ")

