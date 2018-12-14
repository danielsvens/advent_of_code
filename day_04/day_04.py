from datetime import datetime
from pprint import pprint


def get_data():

    data_list = list()

    with open('test_data.txt', 'r') as f:
        for line in f.readlines():
            data_list.append(line.strip())

    return data_list


def part_one(data_list):

    guards = dict()
    guard_id = 0
    #start_time = ''

    for guard in data_list:
        if guard.split()[2] == 'Guard':
            guards.update({int(guard.split()[3].replace('#', '')): {'start_time': [],
                                                                    'shift': []}})

    data_list.sort()

    pprint(data_list)

    for guard in data_list:
        if guard.split()[2] == 'Guard':
            guard_id = int(guard.split()[3].replace('#', ''))
            #start_time = '{} {}'.format(guard.split()[0], guard.split()[1])
        else:
            #guards[guard_id]['start_time'].append(start_time)
            guards[guard_id]['shift'].append('{} {}'.format(guard.split()[0].replace('[', ''),
                                                                  guard.split()[1].replace(']', '')))

    minutes = dict()

    for time in guards.items():
        one = [datetime.strptime(x, '%Y-%m-%d %H:%M') for x in time[1]['shift'][::2]]
        two = [datetime.strptime(x, '%Y-%m-%d %H:%M') for x in time[1]['shift'][1::2]]

        print(len(one), len(two))
        result = [(x.total_seconds() / 60) for x in [b - a for a, b in zip(one, two)]]
        print(result)
        try:
            minutes[time[0]] = max(result)
        except ValueError:
            pass

    print(minutes)
    guard_id = [k * v for k, v in minutes.items() if v == max([int(id) for id in minutes.values()])]

    return guard_id


if __name__ == '__main__':

    data = get_data()
    part_one_result = part_one(data)

    print(part_one_result)

