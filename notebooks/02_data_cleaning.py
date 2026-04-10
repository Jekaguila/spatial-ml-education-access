# Limpieza y preparación inicial de datos

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import seaborn as sns

schools = pd.read_csv("../data/raw/schools.csv")
municipios = gpd.read_file("../data/raw/municipios.geojson")
infra = pd.read_csv("../data/raw/infraestructura.csv")

schools = schools.dropna(subset=["lat", "lon"])
schools["geometry"] = schools.apply(lambda row: Point(row["lon"], row["lat"]), axis=1)
schools_gdf = gpd.GeoDataFrame(schools, geometry="geometry", crs="EPSG:4326")

schools_gdf.plot(figsize=(8,8), markersize=2)
plt.title("Ubicación de escuelas públicas")

schools_gdf.to_file("../data/processed/schools_clean.geojson", driver="GeoJSON")
