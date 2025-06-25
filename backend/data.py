from datetime import datetime
from meteostat import Stations, Monthly, units, Normals
import pandas as pd

# 1. Set time period
start = datetime(1990, 1, 1)
end = datetime(2020, 12, 31)

today = datetime.now()

stations = Stations()
stations = stations.fetch()
stations_in_europe = stations[stations['timezone'].str.contains('Europe')]
europe_station_indexes = stations_in_europe.index.tolist()

#print(stations_in_europe)

data = Normals('02978', 1991, 2020)
data = data.fetch()

print(data)




