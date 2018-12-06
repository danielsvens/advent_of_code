from collections import OrderedDict


# Part One
def get_data():

    input_dict = OrderedDict()

    with open('input_data.txt', 'r') as f:
        for line in f.readlines():
            input_dict.update(
                {line.split()[0][1:]: [tuple(line.split()[2][:-1].split(',')), tuple(line.split()[3].split('x'))]})

    return input_dict


def total_fabric():
    return [['.'] * 1000 for _ in range(1000)]


def claim(grid, kordinates, claim):
    kord_1, kord_2 = int(kordinates[0]), int(kordinates[1])
    claim_1, claim_2 = int(claim[0]), int(claim[1])
    constant_1, constant_2 = int(kordinates[0]), int(kordinates[1])

    for _ in range(claim_1 * claim_2):
        if grid[kord_1][kord_2] == '#':
            grid[kord_1][kord_2] = '0'
        else:
            grid[kord_1][kord_2] = '#'
        kord_2 += 1
        if kord_2 == constant_2 + claim_2:
            kord_1 += 1
            kord_2 = constant_2


if __name__ == '__main__':
    fabric_grid = total_fabric()
    claims = get_data()
    for fabric in claims.items():
        claim(fabric_grid, fabric.__getitem__(1)[0], fabric.__getitem__(1)[1])

    obj = '0'

    print(fabric_grid.count(obj))

