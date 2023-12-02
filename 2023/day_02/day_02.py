from functools import reduce

CONFIGURATION = {'red': 12, 'green': 13, 'blue': 14}

def get_input() -> list[str]:
    with open('input.txt') as f:
        return reduce(lambda x, y: x | y, [map_input(game) for game in [l.strip() for l in f.readlines()]], {})
    
def map_input(game: str) -> dict:
    key, val = game.split(':')
    return {int(key.split(' ')[1]): val.strip()}

def split_values(val):
    games = val.split('; ')
    result = dict()
    for game in games:
        cubes = game.split(', ')
        split_cubes =[cube.split(' ') for cube in cubes]
        
        for v, k in split_cubes:
            result |= pick_largest(result, k, int(v))

    return result

def pick_largest(games, k, v):
    if not games.get(k):
        return {k: v}

    if games[k] > v:
        return games
    
    return {k: v}

def approve(game, config_key, config_value):
    if game[config_key] <= config_value:
        return True
    
    return False
    
def part_1():
    games = get_input()
    result = []
    
    for k, v in games.items():

        approved = []
        for config_key, config_value in CONFIGURATION.items():
            game = split_values(v)
            approved.append(approve(game, config_key, config_value))

        if all(approved):
            result.append(k)
    
    print(sum(result))

def part_2():
    ...

if __name__ == '__main__':
    part_1()
    #part_2()