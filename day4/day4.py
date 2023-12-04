from typing import List, Set

path = 'input.txt'
result = 0

# open intput file
with open(path, 'r') as f:
    # read each line
    for line in f:
        # variable declares
        games: str

        # we only care about the games, discard the card info
        _, games = line.strip().split(":")

        # create a list containing two sets, one set for the winning numbers and
        # one set for the card numbers
        lists: List[Set] = [
            set(
                # filter out any list items with null strings
                filter(
                    # function returns true when an item containing no digits
                    # i.e. only spaces is found
                    lambda c: c != '', no_list.strip().split(" ")
                       )
            ) for no_list in games.split(" | ")
        ]

        # find the intersection between winning numbers and
        # card numbers
        common_items = lists[0] & lists[1]

        # if more than one winning number is found, output the score
        # is doubled for each extra number i.e. 1 match = 1, 2 matches = 2
        # three matches = 8 ...
        if len(common_items) > 0:
            print(f"{len(common_items)} {pow(2, len(common_items)-1)}")
            result += pow(2, len(common_items)-1)


print(result)