import pandas

dataFrame = pandas.read_csv("edades-30Alumnos.csv")

valores = list(dataFrame['fi'])

def analisis_estadistico(lista):
    
    df = pandas.DataFrame({"edades": lista, "fi": pandas.Series(lista).value_counts().sort_index()})

    #Cargamos el archivo csv en un DataFrame con pandas.
    # Considerando que el archivo csv tiene una columna llamada 'fi' que representa la frecuencia absoluta de cada dato, nos queda calcular la frecuencia acumulada, que es la suma total de los valores de la frecuencia absoluta.

    df["Fi"] = df["fi"].cumsum()

    # Frecuencia relativa, es la cada frecuencia absoluta obtenidad, dividida por la suma total de la cantidad de datos, es decir, la frecuencia absoluta de cada dato dividida por la suma total de las frecuencias absolutas.
    df["ri"] = df["fi"] / df["fi"].sum()

    # Frecuencia acumulada de la frecuencia relativa, es la suma acumulada de las frecuencias relativas.
    df["Ri"] = df["ri"].cumsum()

    # Frecuencia relativa porcentual, es la frecuencia relativa multiplicada por 100.
    df["pi%"] = df["ri"] * 100

    # Frecuencia acumulada de la frecuencia relativa porcentual, es la suma acumulada de las frecuencias relativas porcentuales.
    df["Pi%"] = df["pi%"].cumsum()

    print("Se ha copiado al portapapeles el siguiente df:")
    print(df)
    
    
analisis_estadistico(valores)
