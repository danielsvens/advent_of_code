from itertools import cycle

# Part One
frequency = 0

with open('input_data.txt', 'r') as f:
    for n in f:
        frequency += int(n)

print('Part one answer: {}'.format(frequency))


# Part Two
def run():

    freq = 0
    found = []
    input_data = cycle(open('input_data.txt'))

    while True:
        for num in input_data:
            found.append(freq)
            freq += int(num)

            if freq in found:
                return freq


print('Part two answer: {}'.format(run()))
