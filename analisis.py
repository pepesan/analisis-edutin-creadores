import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV en un DataFrame
df = pd.read_csv("edutin.csv")

# # Imprime la información del DataFrame
# print(df.info())
# # Obtén información descriptiva de las variables numéricas
# print(df.describe())

# Calculate the average number of rows per course
average_rows_per_course = df.groupby('curso')['curso'].count().mean()

# Print the average rows per course
print(f"La media de filas por curso que aparecen en el listado es: {average_rows_per_course:.2f}")

# Count the number of times each canal appears in the dataframe
canal_counts = df['Canal'].value_counts()

# Sort the canal counts in descending order
sorted_canal_counts = canal_counts.sort_values(ascending=False)

# Print the sorted list of canals
print("Listado de canales ordenados según el número de filas donde aparece:")
print(sorted_canal_counts)

# Count the number of times each Nombre del curso donde lo han metido appears in the dataframe
curso_counts = df['curso'].value_counts()

# Sort the CursoId counts in descending order
sorted_curso_counts = curso_counts.sort_values(ascending=False)

# Print the sorted list of CursoId
print("Listado de Nombre del curso donde lo han metido ordenados según el número de filas donde aparece:")
print(sorted_curso_counts)

# 1. Listado de cursos ordenados por número de veces que aparece
cursos_conteo = df['curso'].value_counts().reset_index(name='Conteo').sort_values(by='Conteo', ascending=False)
print("Listado de cursos ordenados por apariciones:")
print(cursos_conteo)

# 2. Listado de canales presentes ordenados por número de veces que aparece
canales_conteo = df['Canal'].value_counts().reset_index(name='Conteo').sort_values(by='Conteo', ascending=False)
print("Listado de canales ordenados por apariciones:")
print(canales_conteo)


# 3. Función para buscar cursos y URLs por canal
def cursos_por_canal(canal):
    cursos_filtrados = df[df['Canal'] == canal]
    cursos_lista = cursos_filtrados['curso'].tolist()
    urls_por_curso = cursos_filtrados.groupby('curso')['URL_original'].apply(list).to_dict()
    return {"Cursos": cursos_lista, "URLs por Curso": urls_por_curso}


# 4. Prueba de la función para el canal "Universitat Politècnica de València - UPV"

def videos_por_canal(canal):
    resultado_canal = cursos_por_canal(canal)
    print(f"\nCursos del canal {canal}:")
    if resultado_canal["Cursos"]:
        cursos_unicos = ", ".join(set(resultado_canal["Cursos"]))
        print(f"  - {cursos_unicos}")
        print("  URLs por curso:")
        for curso, urls in resultado_canal["URLs por Curso"].items():
            print(f"    - {curso}")
            for url in urls:
                print(f"      - {url}")
    else:
        print("  El canal no se encuentra en el listado")


canal_buscar = "10 Minutos Programando"
videos_por_canal(canal_buscar)

# Listado de canales presentes ordenados por número de veces que aparece
canales_conteo = df['Canal'].value_counts().reset_index(name='Conteo').sort_values(by='Conteo', ascending=False)
print("Listado de canales diferentes:")
print(canales_conteo)
# Print all rows of the DataFrame using to_string()
print(canales_conteo.to_string())

def recorrer_canales(canales_conteo):
  """Iterates through channels in a DataFrame and calls videos_por_canal for each channel.

  Args:
    canales_conteo: A pandas DataFrame containing channel information,
      including a 'Canal' column for channel names.
  """

  for index, row in canales_conteo.iterrows():
    canal_nombre = row["Canal"]
    videos_por_canal(canal_nombre)


recorrer_canales(canales_conteo)
