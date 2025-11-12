from datetime import datetime
from meteostat import Stations, Monthly, units, Normals
import pandas as pd
import os
path = os.path.dirname(os.path.abspath(__file__))

# 1. Set time period
start = datetime(1990, 1, 1)
end = datetime(2020, 12, 31)

today = datetime.now()
'''

stations = Stations()
stations = stations.fetch()
stations_in_europe = stations[stations['timezone'].str.contains('Africa')]
stations_in_europe = stations_in_europe[['name', 'country']]

stations_in_europe.to_csv('africa_stations', sep=';', encoding='utf-8')
'''
'''
df = pd.read_csv(f'weather_data/africa_stations.csv', sep=';')

data = Normals(stations_indexes[0][0], 1991, 2020)
data = data.fetch()


data['id'] = stations_indexes[0][0]
data.set_index('id', inplace=True)
data.insert(loc=0, column='normal_month', value=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
data.insert(loc=1, column='name', value=stations_indexes[0][1])
data.insert(loc=2, column='country', value=stations_indexes[0][2])

print(stations_indexes)
'''
df = pd.read_csv(f'weather_data/africa_stations.csv', sep=';')
stations_indexes = df.values.tolist()
with open('africa_stations_with_normals.csv', 'a') as f:
    for i in range(1, len(stations_indexes)):
        try:
            moi = Normals(stations_indexes[i][0], 1991, 2020)
            station = moi.fetch()
            f.write(f'{stations_indexes[i][0]};{stations_indexes[i][1]};{stations_indexes[i][2]}' + '\n')
            print(f'{stations_indexes[i][0]};{stations_indexes[i][1]};{stations_indexes[i][2]}')
        except:
            continue


