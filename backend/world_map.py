import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def plot_map(month, temperature):
    df = pd.read_csv('weather_data/europe_station_normals.csv')
    df = df.drop(df[df['country']=='RU'].index) # drop Russia
    df = df.drop(df[df['country']=='UA'].index) # drop Ukraine
    df = df.drop(df[df['country']=='BY'].index) # drop Belarus
    df = df.loc[(df['tmax'] > temperature) & (df['normal_month'] == month)]

    print(df)

    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df['longitude'], df['latitude']), crs="EPSG:4326"
    )

    world = gpd.read_file('static/maps/110m_cultural/ne_110m_admin_0_countries.shp')

    europe = world[(world['CONTINENT'] == 'Europe') | (world['CONTINENT'] == 'Africa')]

    #gdf = gpd.sjoin(gdf, europe[['geometry']], how='inner', predicate='within')

    ax = europe.plot(color="white", edgecolor="black", figsize=(12,12))

    ax.set_xlim(-25, 45)
    ax.set_ylim(25, 75)

    for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['name'] + ' (' + gdf['tmax'].astype(str) + ')'):
        ax.text(x + 0.02, y + 0.02, label, fontsize=10)

    gdf.plot(ax=ax, color='red', markersize=10)

    plt.show()

def gui():
    while True:
        user_input = input("Enter month and minimum temperature: ")
        if user_input == "":
            break
        user_input = user_input.split()
        month = float(user_input[0])
        temperature = float(user_input[1])
        plot_map(month, temperature)

gui()




