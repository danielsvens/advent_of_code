
def get_input() -> list[str]:
    with open('input.txt') as f:
        return [l.strip() for l in f.readlines()]
    
NUMBERS = ''.join([str(i) for i in range(0, 10)])
WORD_TO_NUMBER = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def find_digit(value):
    word = ''
    for c in value:
        if c in NUMBERS:
            return c

        word += c
        for k in WORD_TO_NUMBER.keys():
            if k in word[::-1] or k in word:
                return WORD_TO_NUMBER[k]

def part_1():
    inpt = get_input()
    values = []

    for val in inpt:
        temp = ''

        for char in val:
            if char in NUMBERS:
                temp += char
        
        values.append(f'{temp[0]}{temp[-1]}')

    print(sum(map(int, values)))

def part_2():
    print(sum(map(int, [f'{find_digit(val)}{find_digit(val[::-1])}' for val in get_input()])))

if __name__ == '__main__':
    part_1()
    part_2()
