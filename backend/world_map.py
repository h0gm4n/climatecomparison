import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geodatasets import get_path

df = pd.read_csv('weather_data/europe_station_normals.csv')

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df['longitude'], df['latitude']), crs="EPSG:4326"
)

world = gpd.read_file('static/maps/110m_cultural/ne_110m_admin_0_countries.shp')

europe = world[world['CONTINENT'] == 'Europe']

gdf = gpd.sjoin(gdf, europe[['geometry']], how='inner', predicate='within')

ax = europe.plot(color="white", edgecolor="black", figsize=(8,8))

# Plot points
gdf.plot(ax=ax, color='red', markersize=5)

# --- LIMIT VIEW TO EUROPE BOUNDS ---
minx, miny, maxx, maxy = europe.total_bounds
ax.set_xlim(-25, 45)
ax.set_ylim(34, 75)

plt.show()



