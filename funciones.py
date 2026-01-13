import pandas as pd
import matplotlib.pyplot as plt

minutos_minimos = 500 #Filtro jugadores con pocos minutos jugados
partidos_minimos = 41 #Filtro jugadores con pocos partidos jugados

def extraer_datos(ruta_archivo):
    # Cargar los datos desde un archivo CSV
    datos = pd.read_csv(ruta_archivo)
    
    # Filtrar jugadores con minutos jugados mayores o iguales a minutos_minimos
    datos_filtrados = datos[datos['mp'] >= minutos_minimos]
    datos_filtrados = datos_filtrados[datos_filtrados['g'] >= partidos_minimos]
    
    return datos_filtrados

datos = pd.DataFrame(extraer_datos('Advanced.csv'))

print(datos.head())  # Mostrar las primeras filas del DataFrame para verificar la carga de datos