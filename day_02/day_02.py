from collections import Counter

# Part One
id_list = []

with open('input_data.txt', 'r') as box_ids:
    for id in box_ids:
        id_list.append(id.strip())


def part_1():
    ids = [Counter(id) for id in id_list]

    two = 0
    three = 0

    for item in ids:
        if 3 in item.values():
            three += 1
        if 2 in item.values():
            two += 1

    return two * three


# Part two
first_half, second_half = id_list[:len(id_list)//2], id_list[len(id_list)//2:]


def part_2(f, s):
    box_ids = [z1 != z2 for z1, z2 in zip(f, s)]
    counter = [':parrot:' for i in box_ids if i is True]

    if len(counter) < 2:
        return True


if __name__ == '__main__':

    print(part_1())

    for f in first_half:
        for s in second_half:
            if part_2(f, s):
                print(''.join([z1 for z1, z2 in zip(f, s) if z1 == z2]))
