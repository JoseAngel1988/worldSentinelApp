import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium



data=pd.read_excel('C:/Users/Jose Angel/Desktop/Bootcamp_AI/AI/Curso_PY/PROYECTO/alertaDeforestacion2021.xlsx')

print(data.describe())


areas_deforestadas = data[data['RANGO_AREA'].str.contains('HECTAREAS')]

areas_por_periodo = areas_deforestadas.groupby('PERIODO')['Area_Ha'].sum()


print(areas_por_periodo)


print("Áreas deforestadas por período:")
print(areas_por_periodo)

# Datos de ejemplo (reemplaza esto con tus datos reales)
longitud = [71.686965, 71.856679, 71.850773, 71.738926, 71.882279]
latitud = [2.804070, 2.761626, 2.756696, 2.754243, 2.748895]

# Crear el gráfico de dispersión
plt.scatter(longitud, latitud, c='b', marker='o', label='Áreas deforestadas')

# Etiquetas de los ejes
plt.xlabel('Longitud')
plt.ylabel('Latitud')

# Título del gráfico
plt.title('Ubicación de áreas deforestadas')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

# Datos de ejemplo (reemplaza esto con tus datos reales)
periodos = ["1er Trimestre", "2do Trimestre", "3er Trimestre"]
valores = [6296.76, 270.90, 466.11]

# Crear el gráfico de líneas
plt.plot(periodos, valores, marker='o', color='r', label='Área deforestada')

# Etiquetas de los ejes
plt.xlabel('Período')
plt.ylabel('Área (hectáreas)')

# Título del gráfico
plt.title('Tendencia de deforestación por trimestre')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()

print(data.head())

print(data.info())

#/////////////////////////////////////////#


mi_mapa = folium.Map(location=[4.15, -74.08], zoom_start=6)  

for lat, lon in zip(latitud, longitud):
    folium.Marker([2.48, -71.41], popup='Área deforestada').add_to(mi_mapa)
    folium.Marker([2.45, -71.51], popup='Área deforestada').add_to(mi_mapa)
    folium.Marker([2.22, -72.12], popup='Área deforestada').add_to(mi_mapa)
    folium.Marker([2.21, -73.35], popup='Área deforestada').add_to(mi_mapa)
    folium.Marker([2.22, -73.10], popup='Área deforestada').add_to(mi_mapa)
    folium.Marker([2.21, -72.17], popup='Área deforestada').add_to(mi_mapa)
    folium.Marker([2.22, -72.24], popup='Área deforestada').add_to(mi_mapa)

mi_mapa.save('mapa_deforestacion.html')