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

with open(path, 'r') as f:
    # read each line in file
    for line in f:
        # get the game number based on location of :
        game_no = int(line[:line.find(':')].replace('Game ', ''))

        # assume game is valid until we find otherwise
        valid_game = True

        for game_round in line[line.find(':')+2:].split(';'):
            # create a dict to store the colours
            colours = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }

            # set the colours
            for colour in game_round.split(','):
                colours[colour.strip().split()[1]] = int(colour.strip().split()[0])

            # check compare each colour to the test quantities
            # stop checking if exceeded
            for k in test.keys():
                if colours[k] > test[k]:
                    break
            else:
                # move to the next round if round is valid
                continue

            # we reach this line if we break out of the previous loop,
            # that means we should break out of this one
            break
        else:
            # all rounds passed the test, this is a valid game
            valid_games_sum += game_no


print (valid_games_sum)
