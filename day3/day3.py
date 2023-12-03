from typing import List, Tuple, Dict


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


def main():
    # step 1) load the input file into a 2D matrix
    path = 'input.txt'
    matrix = load_file_to_matrix(path)

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
    valid_number_total: int = 0

    gears: Dict[Tuple[int, int], (int, None)] = {}
    cur_gear: (Tuple[int, int], None) = None
    gear_ratio_total: int = 0

    # initilise a buffer to hold numeric digits as they are found
    cur_number_c = ''

    # inisilise a flag which indicates whether a number is valid
    valid_number = False

    # step 2) step through the matrix one cell at a time
    for y in range(y_len):
        for x in range(y_len):
            # obtain the character to test
            c = matrix[y][x]

            # check if the character is a digit
            if c.isdigit():
                # add to the number buffer
                cur_number_c += c

                # step 3) where a number is found, look for a symbol in the surrounding co-ordinates;
                # it the symbol is found mark as valid.
                # check each of the surrounding cells for symbols and gears (*)
                for x_off, y_off in adjacent_offsets:
                    x_chk = x + x_off
                    y_chk = y + y_off

                    # check for invalid co-ordinates and skip if not valid
                    if (x_chk < 0) or (y_chk < 0) or (x_chk >= x_len) or (y_chk >= y_len):
                        continue

                    # if a symbol is found, mark as valid
                    if is_symbol(matrix[y_chk][x_chk]):
                        valid_number = True

                        # for the second part check if the symbol is a (*) - gear
                        if matrix[y_chk][x_chk] == '*':
                            # record the current gear
                            cur_gear = (x_chk, y_chk)

                            # add it to the list it doesn't exist
                            if cur_gear not in gears:
                                gears[cur_gear] = None

            if (not c.isdigit()) or (x == x_len - 1):
                # step 4) stop reading the number when a non numeric character is encountered or
                # at the end of the row

                if cur_number_c != '':
                    # a non-numeric character immediately after a number indicates the end of
                    # a string of number characters
                    cur_number = int(cur_number_c)

                    # add the number fo the total if it is valid and print the number
                    valid_number_total += process_number(cur_number_c, valid_number)

                    if cur_gear is not None:
                        # if there is a current gear, add this number to the list for that gear
                        if gears[cur_gear] is not None:
                            gear_ratio_total += gears[cur_gear] * cur_number
                        else:
                            gears[cur_gear] = cur_number

                        cur_gear = None

                    # reset the buffer and flag
                    cur_number_c = ''
                    valid_number = False

                # print the current character
                print(c, end='')

        else:
            # print a new line as at end of line
            print('')

    print(f"Part 1: {valid_number_total}")
    print(f"Part 2: {gear_ratio_total}")


main()
