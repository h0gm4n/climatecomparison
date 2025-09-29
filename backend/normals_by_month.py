from datetime import datetime
from meteostat import Stations, Monthly, units, Normals
import pandas as pd
import os
path = os.path.dirname(os.path.abspath(__file__))


df = pd.read_csv(f'weather_data/europe_stations_with_normals', delimiter=';')

first_id = df.iloc[0]['id']

first_normal = Normals(first_id, 1991, 2020)
first_normal = first_normal.fetch()

first_normal.insert(0, 'id', first_id)
first_normal.insert(1, 'name', df.iloc[0]['name'])
first_normal.insert(2, 'country', df.iloc[0]['country'])
first_normal.insert(3, 'normal_month', first_normal.index)
first_normal.set_index('id', inplace=True)

"""
second_id = df.iloc[1]['id']
second_normal = Normals(second_id, 1991, 2020)
second_normal = second_normal.fetch()
second_normal.insert(0, 'id', second_id)
second_normal.insert(1, 'name', df.iloc[1]['name'])
second_normal.insert(2, 'country', df.iloc[1]['country'])
second_normal.insert(3, 'normal_month', second_normal.index)
second_normal.set_index('id', inplace=True)
all_normals = pd.concat([first_normal, second_normal])

for index, row in df.iloc[2:].iterrows():
    station_id = row['id']
    try:
        normal = Normals(station_id, 1991, 2020)
        normal = normal.fetch()
        normal.insert(0, 'id', station_id)
        normal.insert(1, 'name', row['name'])
        normal.insert(2, 'country', row['country'])
        normal.insert(3, 'normal_month', normal.index)
        normal.set_index('id', inplace=True)
        all_normals = pd.concat([all_normals, normal])
        print(f'Added normals for station {station_id} - {row["name"]}')
    except Exception as e:
        print(f'Could not fetch normals for station {station_id} - {row["name"]}: {e}')

all_normals.to_csv('europe_station_normals.csv')
"""
print(first_normal)