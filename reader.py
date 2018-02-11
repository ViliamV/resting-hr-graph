import os
import csv
from datetime import date
from dateutil.parser import parse

def read_data():
    data = {}
    path = f'{os.getcwd()}/data'
    files = os.listdir(path)
    for ff in files:
        if ff.endswith('.csv') or ff.endswith('.CSV'):
            with open(f'{path}/{ff}') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    row_date = parse(row['dateTime'], dayfirst=True, yearfirst=False).date()
                    row_hr = row['rate']
                    if row_date in data:
                        data[row_date].append(int(row_hr))
                    else:
                        data[row_date] = [int(row_hr)]

    x, y = [], []
    for k, v in data.items():
        x.append(k)
        y.append(min(v))
    return x, y
