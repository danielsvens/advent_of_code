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


def claim(grid, coordinates, claim):

    kord_1, kord_2 = int(coordinates[0]), int(coordinates[1])
    claim_1, claim_2 = int(claim[0]), int(claim[1])
    constant_1, constant_2 = int(coordinates[0]), int(coordinates[1])

    for _ in range(claim_1 * claim_2):
        if grid[kord_1][kord_2] == '#':
            grid[kord_1][kord_2] = '0'
        elif grid[kord_1][kord_2] == '0':
            grid[kord_1][kord_2] = '0'
        else:
            grid[kord_1][kord_2] = '#'
        kord_2 += 1
        if kord_2 == constant_2 + claim_2:
            kord_1 += 1
            kord_2 = constant_2


def unique(grid, claim_id, coordinates, claim):

    id = claim_id
    kord_1, kord_2 = int(coordinates[0]), int(coordinates[1])
    claim_1, claim_2 = int(claim[0]), int(claim[1])
    constant_1, constant_2 = int(coordinates[0]), int(coordinates[1])
    counter = 0

    for _ in range(claim_1 * claim_2):
        if grid[kord_1][kord_2] == '#':
            counter += 1
        kord_2 += 1
        if kord_2 == constant_2 + claim_2:
            kord_1 += 1
            kord_2 = constant_2

        if counter == claim_1 * claim_2:
            print('#{}'.format(id))


if __name__ == '__main__':
    overlap = 0
    fabric_grid = total_fabric()
    claims = get_data()
    for inches in claims.items():
        claim(fabric_grid, inches.__getitem__(1)[0], inches.__getitem__(1)[1])

    for i in fabric_grid:
        overlap += i.count('0')

    print(overlap)

    # Part two
    for inches in claims.items():
        unique(fabric_grid, inches[0], inches.__getitem__(1)[0], inches.__getitem__(1)[1])
