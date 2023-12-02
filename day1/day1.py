replacements = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_no_with_text(text: str):
    # place holder variables for digits found
    digit_1 = digit_2 = ''

    # loop through the string one character at a time
    for x in range(len(text)):
        # check if this character is a digit or the string up to this point is a number
        if digit_1 == '':
            if text[x:x+1].isdigit():
                digit_1 = text[x:x+1]
            else:
                for k in replacements.keys():
                    if k in text[:x+1]:
                        digit_1 = replacements[k]
                        break

        # do the same but from the end of the string
        if digit_2 == '':
            if text[-(x+1)].isdigit():
                digit_2 = text[-(x+1)]
            else:
                for k in replacements.keys():
                    if k in text[-(x+1)::1]:
                        digit_2 = replacements[k]
                        break

        # if we have both digits - stop checking
        if digit_1 != '' and digit_2 != '':
            break

    return int('0' + digit_1 + digit_2)


def get_no_simple(text: str):
    digit_1 = digit_2 = ''

    for c in text:
        if c.isdigit():
            digit_1 = c
            break

    for c in text[::-1]:
        if c.isdigit():
            digit_2 = c
            break

    return int(digit_1 + digit_2)


path = 'input.txt'

result1 = 0
result2 = 0

# open intput file
with open(path, 'r') as f:
    # read each line
    for line in f:
        no_1 = get_no_simple(line)
        no_2 = get_no_with_text(line)

        result1 += no_1
        result2 += no_2

print(result1)
print(result2)
