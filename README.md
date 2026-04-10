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

Spatial ML for Education Access: Inteligencia Geográfica para la Equidad Educativa
📌 Resumen Ejecutivo
En muchas naciones, la ubicación geográfica de un estudiante determina su destino académico. Este proyecto utiliza Machine Learning y Sistemas de Información Geográfica (GIS) para analizar la accesibilidad física a las escuelas públicas y detectar patrones espaciales de desigualdad educativa.
El objetivo principal es identificar "zonas rojas" de exclusión y proporcionar insumos basados en datos para el diseño de políticas públicas, planificación de transporte y ubicación de nueva infraestructura escolar.

🔍 Preguntas de Investigación
•	¿Qué tan accesibles son las escuelas públicas según su ubicación geográfica real? 
•	¿Existen patrones espaciales que correlacionen la baja accesibilidad con indicadores de pobreza? 
•	¿Qué factores socioeconómicos y geográficos predicen un menor acceso a servicios educativos de calidad? 
🛠️ Metodología y Stack Técnico
El proyecto se divide en fases críticas que integran el rigor pedagógico con la potencia computacional:
1.	Análisis Espacial (GIS): Uso de Kernel Density Estimation (KDE) para identificar densidades escolares y Moran’s I para validar la autocorrelación espacial de la desigualdad.
2.	Machine Learning Supervisado: Modelos de Random Forest y XGBoost para predecir niveles de accesibilidad basados en infraestructura vial y densidad poblacional.
3.	Clustering No Supervisado: Implementación de DBSCAN y HDBSCAN para identificar cúmulos geográficos de vulnerabilidad educativa.
4.	Visualización de Impacto: Mapas interactivos con Folium y dashboards en Power BI/Streamlit para tomadores de decisiones.
Core Stack
•	Lenguaje: Python (GeoPandas, Scikit-learn, Shapely, PySAL).
•	Geo-Data: OpenStreetMap, capas de red vial y datos censales.

📊 Hallazgos Clave (Preview)
(Aquí incluirás una captura de tus mapas de calor o clusters una vez generados).
•	Desigualdad Territorial: Se identificaron brechas significativas en zonas rurales donde la distancia promedio supera los 5 km por red vial.
•	Correlación Crítica: Existe una correlación de $r = 0.XX$ entre la falta de infraestructura de transporte y el rendimiento académico en zonas periféricas.
