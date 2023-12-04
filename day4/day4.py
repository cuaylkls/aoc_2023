from typing import List, Set

path = 'input.txt'
result = 0

# create a dict to hold the total number of cards
# including copies held, indexed using card no
cards_held = {}

# open intput file
with open(path, 'r') as f:
    # read each line
    for line in f:
        # variable declares
        card_str: str
        games: str

        # get the card number and game info
        card_str, games = line.strip().split(":")
        card_no = int(card_str.replace("Card", "").strip())

        # set and get the total number of cards held
        # where there are no cards held, set to 1 for the current card
        cards_held[card_no] = total_of_card = (cards_held[card_no] if card_no in cards_held else 0) + 1

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
        total_common = len(common_items)
        if total_common > 0:

            # for the first result
            result += pow(2, total_common-1)

            # for the second result, move forward by the number of matches in the game
            # adding the next cards in the sequence. Where the card already exists in the
            # dict increment the value
            for card_copy_no in range(card_no + 1, card_no + 1 + total_common):
                cards_held[card_copy_no] = (
                                               cards_held[card_copy_no] if card_copy_no in cards_held else 0
                                           ) + total_of_card

print(f"Result 1: {result}")
print(f"Result 2: {sum(cards_held.values())}")
