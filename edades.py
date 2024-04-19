import pandas as pd

# Lista de las edades de los alumnos
edades = [18, 19, 20, 21, 22, 23, 25, 28, 29, 30, 34]


def analisis_estadistico(edades):
    # Verificar si edades no es una lista o está vacía, si es así, imprimir mensaje de error.
    if not isinstance(edades, list) or len(edades) == 0:
        print("La lista de edades está vacía o el parámetro no es una lista")
        return None
    # Frecuencia Simple: Veces que se repiten esas edades, en el mismo orden.

    # Verificar si todas las edades son numéricas, en caso de que no sea así, imprimir mensaje de error.
    if not all(isinstance(x, (int, float)) for x in edades):
        print("La lista de edades contiene elementos que no son numéricos.")
        return None

    # Crear DataFrame con las listas proporcionadas
    df = pd.DataFrame({"edades": edades, "fi": fi})

    # Calcular Frecuencia absoluta acumulada: Suma de las frecuencias absolutas de las edades anteriores.
    df["Fi"] = df["fi"].cumsum()
    # Calcular Frecuencia relativa simple: Frecuencia absoluta de una edad dividida entre la suma de todas las frecuencias absolutas.
    df["ri"] = (df["fi"] / df["fi"].sum()).round(3)
    # Calcular Frecuencia relativa acumulada: Suma de las frecuencias relativas de las edades anteriores.
    df["Ri"] = df["ri"].cumsum()
    # Calcular Frecuencia porcentual simple: Frecuencia relativa simple multiplicada por 100.
    df["pi%"] = df["ri"] * 100
    # Calcular Frecuencia porcentual acumulada: Suma de las frecuencias porcentuales de las edades anteriores.
    df["Pi%"] = df["pi%"].cumsum()

    return df


# Crear DataFrame y aplicar análisis estadístico
print(analisis_estadistico(edades))
