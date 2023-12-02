



def main():

    game_data = {}

    with open ('puzzle2.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n', '')
            id_data_split = line.split(':')
            game_id = int(id_data_split[0].split(' ')[1])
            game_sets = id_data_split[1].split(';')
            game_data[game_id] = []
            for count, game in enumerate(game_sets):
                game_object = {}
                cube_pairs = game.split(',')
                for pair in cube_pairs:
                    pair = pair.split(' ')
                    amount = int(pair[1])
                    color = pair[2]
                    game_object[color] = amount
                game_data[game_id].append(game_object)

            line = f.readline()


    possible_games = []
    allowed_amounts = {
        'red': 12,
        'blue': 14,
        'green': 13,
    }
    for i in range(1,101):
        game_possible = True
        current_game_sets = game_data[i]
        print(current_game_sets)
        smallest_possible = {}

        for game in current_game_sets:
            for color in game.keys():
                if color not in smallest_possible.keys():
                    smallest_possible[color] = game[color]
                else:
                    if smallest_possible[color] < game[color]:
                        smallest_possible[color] = game[color]
        game_set_power = 1
        print(smallest_possible)
        
        for value in smallest_possible.values():
            game_set_power *= value
        print(game_set_power)
        print('-----------\n')
        possible_games.append(game_set_power)
        

    return sum(possible_games)

if __name__ == "__main__":
    print(main())