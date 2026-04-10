# Ingeniería de Caraterísticas Especiales
import geopandas as gpd
import numpy as np
from sklearn.neighbors import BallTree

def compute_nearest_school_distance(households_gdf, schools_gdf):
    schools_coords = np.radians(np.c_[schools_gdf.geometry.y, schools_gdf.geometry.x])
    households_coords = np.radians(np.c_[households_gdf.geometry.y, households_gdf.geometry.x])
    tree = BallTree(schools_coords, metric='haversine')
    distances, _ = tree.query(households_coords, k=1)
    households_gdf['nearest_school_km'] = distances * 6371
    return households_gdf

def compute_school_density(df, schools, radius_km=5):
    df = df.copy()
    df["school_density"] = 0
    for idx, row in df.iterrows():
        buffer = row.geometry.buffer(radius_km / 111)
        df.loc[idx, "school_density"] = schools.within(buffer).sum()
    return df

df["accessibility_index"] = (
    1 / (1 + df["nearest_school_km"])
) * (df["school_density"] + 1)

df.to_file("../data/processed/features.geojson", driver="GeoJSON")
