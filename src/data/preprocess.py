"""
preprocess.py
---------------------------------------
Módulo de limpieza y preparación inicial de datos
para el proyecto Spatial ML for Education Access.

Incluye:
- Carga de datos crudos
- Limpieza de nulos
- Validación de columnas
- Conversión a GeoDataFrame
- Validación de coordenadas
- Guardado en /data/processed/

Autor: Jessica Liset Martínez de Águila
Proyecto: Spatial ML for Education Access
"""

import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point


# ---------------------------------------------------------
# 1. Función para cargar datos
# ---------------------------------------------------------
def load_raw_data(path: str) -> pd.DataFrame:
    """
    Carga un archivo CSV desde la carpeta /data/raw/.

    Parámetros:
        path (str): ruta del archivo CSV.

    Retorna:
        pd.DataFrame: dataframe cargado.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo no existe: {path}")

    df = pd.read_csv(path)
    print(f"Archivo cargado correctamente: {path}")
    print(f"Dimensiones: {df.shape}")
    return df


# ---------------------------------------------------------
# 2. Validación de columnas requeridas
# ---------------------------------------------------------
def validate_columns(df: pd.DataFrame, required_cols: list):
    """
    Verifica que el dataframe contenga las columnas necesarias.

    Parámetros:
        df (pd.DataFrame): dataframe a validar
        required_cols (list): lista de columnas requeridas
    """
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")
    print("Columnas validadas correctamente.")


# ---------------------------------------------------------
# 3. Limpieza de nulos
# ---------------------------------------------------------
def clean_nulls(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """
    Elimina filas con valores nulos en columnas críticas.

    Parámetros:
        df (pd.DataFrame)
        subset (list): columnas donde no se permiten nulos

    Retorna:
        pd.DataFrame limpio
    """
    if subset:
        before = df.shape[0]
        df = df.dropna(subset=subset)
        after = df.shape[0]
        print(f"Filas eliminadas por nulos: {before - after}")

    return df


# ---------------------------------------------------------
# 4. Conversión a GeoDataFrame
# ---------------------------------------------------------
def to_geodataframe(df: pd.DataFrame, lon_col="lon", lat_col="lat") -> gpd.GeoDataFrame:
    """
    Convierte un dataframe con columnas lat/lon a GeoDataFrame.

    Parámetros:
        df (pd.DataFrame)
        lon_col (str)
        lat_col (str)

    Retorna:
        gpd.GeoDataFrame
    """
    validate_columns(df, [lon_col, lat_col])

    df["geometry"] = df.apply(lambda row: Point(row[lon_col], row[lat_col]), axis=1)
    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")

    print("Conversión a GeoDataFrame completada.")
    return gdf


# ---------------------------------------------------------
# 5. Validación de coordenadas
# ---------------------------------------------------------
def validate_coordinates(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Elimina puntos fuera de rangos válidos de lat/lon.

    Retorna:
        gpd.GeoDataFrame filtrado
    """
    before = gdf.shape[0]

    gdf = gdf[
        (gdf.geometry.x >= -180) & (gdf.geometry.x <= 180) &
        (gdf.geometry.y >= -90) & (gdf.geometry.y <= 90)
    ]

    after = gdf.shape[0]
    print(f"Coordenadas inválidas eliminadas: {before - after}")

    return gdf


# ---------------------------------------------------------
# 6. Guardado final
# ---------------------------------------------------------
def save_processed(gdf: gpd.GeoDataFrame, filename: str):
    """
    Guarda el GeoDataFrame procesado en /data/processed/.

    Parámetros:
        gdf (gpd.GeoDataFrame)
        filename (str): nombre del archivo de salida
    """
    output_path = f"data/processed/{filename}"

    os.makedirs("data/processed", exist_ok=True)
    gdf.to_file(output_path, driver="GeoJSON")

    print(f"Archivo procesado guardado en: {output_path}")


# ---------------------------------------------------------
# 7. Pipeline principal
# ---------------------------------------------------------
def preprocess_pipeline(input_path: str, output_filename: str):
    """
    Pipeline completo de limpieza y conversión a GeoDataFrame.

    Parámetros:
        input_path (str): ruta del archivo CSV crudo
        output_filename (str): nombre del archivo procesado
    """
    print("Iniciando pipeline de preprocesamiento...")

    df = load_raw_data(input_path)
    df = clean_nulls(df, subset=["lat", "lon"])
    gdf = to_geodataframe(df)
    gdf = validate_coordinates(gdf)
    save_processed(gdf, output_filename)

    print("Pipeline completado exitosamente.")
    return gdf


# Ejemplo de uso:
# preprocess_pipeline("data/raw/schools.csv", "schools_clean.geojson")
