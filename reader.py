import os
import csv
from datetime import date
from dateutil.parser import parse
import itertools
from collections import deque


def moving_average(data, window):
    for i in range(window - 1):
        yield data[i]
    it = iter(data)
    d = deque(itertools.islice(it, window - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / window


def read_data():
    data = {}
    path = f'{os.getcwd()}/data'
    files = os.listdir(path)
    for ff in files:
        if ff.endswith('.csv') or ff.endswith('.CSV'):
            with open(f'{path}/{ff}') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    row_date = parse(
                        row['dateTime'], dayfirst=True,
                        yearfirst=False).date()
                    row_hr = row['rate']
                    if row_date in data:
                        data[row_date].append(int(row_hr))
                    else:
                        data[row_date] = [int(row_hr)]

    cleaned_data = [(k, min(v)) for k, v in data.items()]
    for k, v in data.items():
        cleaned_data.append((k, min(v)))
    from operator import itemgetter
    x, y = [], []
    for c in sorted(cleaned_data, key=itemgetter(0)):
        x.append(c[0])
        y.append(c[1])
    return x, y, list(moving_average(y, 10))
