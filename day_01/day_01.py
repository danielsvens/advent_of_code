from itertools import cycle

# Part One
frequency = 0

with open('input_data.txt', 'r') as f:
    for n in f:
        frequency += int(n)


# Part Two
def part_2():

    freq = 0
    found = set()
    input_data = open('input_data.txt')

    while True:
        for num in cycle(input_data):
            found.add(freq)
            freq += int(num)

            if freq in found:
                return freq


if __name__ == '__main__':
    print(frequency)
    print(part_2())
