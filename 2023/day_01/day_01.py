
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

def find_first(value):
    num = ''
    for c in value:
        if c in NUMBERS:
            return c

        num += c
        for k in WORD_TO_NUMBER.keys():
            if k in num:
                return WORD_TO_NUMBER[k]

def find_last(value):
    num = ''
    for c in value[::-1]:
        if c in NUMBERS:
            return c

        num += c
        for k in WORD_TO_NUMBER.keys():
            if k in num[::-1]:
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
    inpt = get_input()
    values = []

    for val in inpt:
        first = find_first(val)
        last = find_last(val)
        
        values.append(f'{first}{last}')

    print(sum(map(int, values)))


def get_number(char):
    try:
        return int(char)
    except Exception:
        return None

if __name__ == '__main__':
    #part_1()
    part_2()