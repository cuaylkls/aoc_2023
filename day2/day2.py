from functools import reduce

path = 'input.txt'

# test set, games where the number of cubes for that
# colour exceed the below are invalid
test = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# create a variable to hold final result
valid_games_sum = 0
min_values_sum = 0

with open(path, 'r') as f:
    # read each line in file
    for line in f:
        # get the game number based on location of :
        game_no = int(line[:line.find(':')].replace('Game ', ''))

        # assume game is valid until we find otherwise
        valid_game = True

        # dict to store minimum values
        min_values = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        for game_round in line[line.find(':')+2:].split(';'):
            # set the colours
            for colour_spec in game_round.split(','):
                # get each component and set the colour
                colour = colour_spec.strip().split()[1]
                value = int(colour_spec.strip().split()[0])

                # record the maximum value compared to the last round
                min_values[colour] = max(min_values[colour], value)

                # check compare each colour to the test quantities
                # set a flag if game is invalid
                if value > test[colour]:
                    valid_game = False

        # add the game number for valid games
        if valid_game:
            valid_games_sum += game_no

        # add the product of the minimum values to the final value
        min_values_sum += reduce(lambda x, y: x * y, min_values.values())

print(f"Part 1: {valid_games_sum}")
print(f"Part 2: {min_values_sum}")
