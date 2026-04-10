import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def clean_school_data(file_path):
    """
    Carga, limpia y proyecta los datos de ubicación de escuelas.
    """
    # 1. Carga de datos
    df = pd.read_csv(file_path)
    
    # 2. Limpieza de nulos en coordenadas
    # Se eliminan registros que no posean latitud o longitud
    df = df.dropna(subset=['latitud', 'longitud'])
    
    # 3. Validación de rangos geográficos (Filtro para El Salvador)
    # Latitud aproximada: [13.1, 14.5], Longitud: [-90.2, -87.6]
    df = df[(df['latitud'] > 13.0) & (df['latitud'] < 15.0)]
    df = df[(df['longitud'] > -91.0) & (df['longitud'] < -87.0)]
    
    # 4. Creación de geometría GeoPandas
    geometry = [Point(xy) for xy in zip(df['longitud'], df['latitud'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    
    return gdf

if __name__ == "__main__":
    # Ejemplo de uso interno
    data_path = "data/raw/escuelas_raw.csv"
    schools_cleaned = clean_school_data(data_path)
    schools_cleaned.to_file("data/processed/schools_spatial.geojson", driver='GeoJSON')
    print("Fase de limpieza completada con éxito.")
