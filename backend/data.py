from datetime import datetime
from meteostat import Stations, Monthly, units
import pandas as pd

# 1. Set time period
start = datetime(1990, 1, 1)
end = datetime(2020, 12, 31)

# 2. Find nearest weather station to Helsinki
stations = Stations()
stations = stations.nearby(60.1695, 24.9354)  # Helsinki coordinates
station = stations.fetch(1)

#print("Using station:", station.iloc[0]['name'])

#print(station.iloc[0])

data = Monthly(station.iloc[0]['wmo'], start, end)
data = data.fetch()
data = data.groupby(data.index.month).mean()

print(data.get(['tavg', 'tmax', 'tmin']))