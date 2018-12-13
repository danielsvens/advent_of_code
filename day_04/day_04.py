from pprint import pprint
from datetime import datetime

data_list = list()
guards = {}

guard_id = 0
start_time = ''

with open('input_data.txt', 'r') as f:
    for line in f.readlines():
        data_list.append(line.strip())

for guard in data_list:
    if guard.split()[2] == 'Guard':
        guards.update({int(guard.split()[3].replace('#', '')): {'start_time': [],
                                                                'shift': []}})

data_list.sort()

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
    result = [(x.total_seconds() / 60) - 1 for x in [b - a for a, b in zip(one, two)]]
    try:
        minutes[time[0]] = max(result) * time[0]
    except ValueError:
        pass

print(max([int(id) for id in minutes.values()]))








#pprint(guards.items())
