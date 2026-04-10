# Análisis GIS y Geoestadística

#KDE
from sklearn.neighbors import KernelDensity

coords = np.vstack([schools_gdf.geometry.x, schools_gdf.geometry.y]).T
kde = KernelDensity(bandwidth=0.02).fit(coords)

# Morans
import esda
import libpysal

w = libpysal.weights.Queen.from_dataframe(df)
moran = esda.Moran(df["accessibility_index"], w)
moran.I, moran.p_sim

# LISA
lisa = esda.Moran_Local(df["accessibility_index"], w)
df["lisa_cluster"] = lisa.q

# Mapas 
df.plot(column="accessibility_index", cmap="viridis", legend=True)
plt.title("Índice de accesibilidad educativa")


