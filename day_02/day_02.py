from collections import Counter

# Part One
id_list = []

with open('input_data.txt', 'r') as box_ids:
    for id in box_ids:
        id_list.append(id.strip())


def find_letters():
    ids = [Counter(id) for id in id_list]

    two = 0
    three = 0

    for item in ids:
        if 3 in item.values():
            three += 1
        if 2 in item.values():
            two += 1

    return two * three


print(find_letters())
