import geopandas as gpd
import Config


def read_map():
    poland = gpd.read_file(Config.MAP_PATH + "\\poland.geojson")
    return poland
    # poland.plot(column='test', scheme='fisher_jenks', cmap='Reds', k=16)
    # plt.axis('off')
    # plt.show()
