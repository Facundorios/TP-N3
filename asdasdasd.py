import pandas as pd

def analisis_estadistico(l):
    try:

        # Controlamos que el elemento pasado por parametros sea una lista
        if type(l) != list:
            raise TypeError("El parametro recibido no es una lista")

        # Controlamos que la lista no este vacia
        if len(l) == 0:
            raise ValueError("La lista está vacia")
        
        # Controlamos que la lista no contenga valores no numericos
        for element in l:
            if type(element) != int:
                raise TypeError("La lista contiene elementos no numericos")

        # Ordenamos la lista
        l.sort()

        # Creamos un dict con las edades y la frecuencia (fi) de cada una
        fi = {}
        for i in l:
            if i in fi:
                fi[i] += 1
            else:
                fi[i] = 1

        # Convertimos el dict en un dataframe
        df = pd.DataFrame({'edades':fi.keys(),'fi':fi.values()})

        # Calculamos la frecuencia acumulada (Fi) y la frecuencia relativa (ri) de cada una
        df["Fi"] = df["fi"].cumsum()
        df["ri"] = df["fi"] / df["fi"].sum()
        # Calculamos la frecuencia relativa acumulada (Ri) de cada una
        df["Ri"] = df["ri"].cumsum()
        # Calculamos el porcentaje (pi%) y el porcentaje acumulado (Pi%) multiplicando sus respectivas frecuencias relativas por 100
        df["pi%"] = df["ri"] * 100
        df["Pi%"] = df["Ri"] * 100

        return df
    # Controlamos las excepciones que colocamos arriba
    except ValueError as e:
        print(e)
        return None
    except TypeError as e:
        print(e)
        return None

# Estas son 30 edades que consultamos en el curso, se puede cambiar para realizar más pruebas.
edades = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]

print(analisis_estadistico(edades))