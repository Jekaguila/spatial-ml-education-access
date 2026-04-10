# spatial-ml-education-access
spatial-ml-education-access

## Información del Proyecto

- Lugar de aplicación: San Salvador, El Salvador (Escuelas públicas)
- Duración: Junio 2025 – Septiembre 2025
- Entidad: Asociación de Matemáticos de El Salvador / Escuela de Matemática  
- Tipo de proyecto: Investigación aplicada en Machine Learning y análisis geoespacial

## Objetivo
Alizar el acceso a la educación utilizando datos geoespaciales y técnicas de Machine Learning para identificar desigualdades territoriales.

## Componente Geoespacial

- Uso de datos espaciales para evaluar accesibilidad educativa  
- Análisis de distribución geográfica de instituciones educativas  
- Identificación de zonas con menor cobertura  

## Impacto
Este proyecto permite identificar brechas en el acceso educativo, facilitando la toma de decisiones para intervenciones en zonas vulnerables.

Spatial ML for Education Access
🎯 Resumen Ejecutivo
Spatial ML for Education Access es un proyecto de análisis espacial y Machine Learning orientado a evaluar la accesibilidad geográfica a escuelas públicas y detectar patrones territoriales de desigualdad educativa.
Combina GIS, geoestadística, modelos predictivos y visualizaciones interactivas para generar evidencia útil para políticas públicas, planificación escolar y estrategias de equidad educativa.

🧩 Objetivos del Proyecto
Objetivo general: Analizar accesibilidad educativa mediante técnicas de Machine Learning y análisis espacial para identificar desigualdad territorial en el acceso a escuelas públicas.
Preguntas de investigación
- ¿Qué tan accesibles son las escuelas públicas según ubicación geográfica?
- ¿Existen patrones espaciales de desigualdad?
- ¿Qué factores geográficos y socioeconómicos predicen menor acceso educativo?
- ¿Cómo varía la accesibilidad entre zonas urbanas y rurales?

🗂️ Datos Utilizados
Datos principales
- Coordenadas de escuelas públicas
- Matrícula, infraestructura, rendimiento académico
- Capas geográficas:
- carreteras
- transporte público
- densidad poblacional
- zonas rurales/urbanas
- Indicadores socioeconómicos municipales
Procesos aplicados
- Limpieza y normalización
- Geocodificación
- Spatial Join
- Cálculo de distancias:
- euclidiana
- por red vial (si se dispone)
- Feature engineering espacial:
- nearest school distance
- school density
- travel time
- accessibility index

🧠 Metodología
El proyecto sigue un pipeline reproducible:
- Preparación de datos
- Ingeniería de características espaciales
- Análisis GIS y geoestadística
- Modelos de Machine Learning
- Clustering espacial
- Visualización y storytelling
- Documentación técnica y replicabilidad

🗺️ Análisis Espacial (GIS)
Técnicas aplicadas:
- Kernel Density Estimation (KDE)
- Moran’s I (autocorrelación espacial)
- LISA clusters (hotspots de desigualdad)
- Mapas coropléticos
- Mapas interactivos con Folium
Resultados esperados:
- Mapa de accesibilidad por municipio
- Identificación de zonas rojas
- Detección de patrones espaciales significativos

🤖 Modelos de Machine Learning
Modelos supervisados
- Random Forest
- Gradient Boosting
- XGBoost
- Regresión lineal regularizada
Modelos no supervisados
- K-Means
- DBSCAN
- HDBSCAN
- Clustering jerárquico
Métricas
- RMSE / MAE
- Silhouette Score
- Moran’s I aplicado a residuos o clusters

📊 Visualizaciones y Storytelling
Visualizaciones clave:
- Mapa de accesibilidad educativa
- Mapa de densidad de escuelas
- Comparación accesibilidad vs pobreza
- Accesibilidad vs rendimiento académico
- Gráficos comparativos urbano vs rural
Opcional:
- Dashboard en Streamlit
- Dashboard en Power BI
