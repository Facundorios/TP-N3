import pandas as pd

#Accedemos al archivo csv donde tenemos una tabla con los nombres y edades de 30 personas.
dataFrame = pd.read_csv("edades.csv")
edades =  list(dataFrame["fi"])

#Definimos lafuncion principal del archivo:
def analisis_estadistico(lista_edades):

    # Verificamos que la lista no esté vacía.
    if not lista_edades:
        print("Error: La lista está vacía")
    # Verificamos que el argumento proporcionado sea una lista.
    if not isinstance(lista_edades, list):
        print("Error: El argumento proporcionado no es una lista")
    # Verificamos que la lista contenga solo elementos numéricos.
    if not all(isinstance(item, (int, float)) for item in lista_edades):
        print("Error: La lista contiene elementos no numéricos")

    
    # Considerando que el archivo csv tiene una columna llamada 'fi' que representa la frecuencia absoluta de cada dato, nos queda calcular la frecuencia acumulada, que es la suma total de los valores de la frecuencia absoluta.
    dataFrame["Fi"] = dataFrame["fi"].cumsum()

    # Frecuencia relativa, es la cada frecuencia absoluta obtenidad, dividida por la suma total de la cantidad de datos, es decir, la frecuencia absoluta de cada dato dividida por la suma total de las frecuencias absolutas.
    dataFrame["ri"] = dataFrame["fi"] / dataFrame["fi"].sum()

    # Frecuencia acumulada de la frecuencia relativa, es la suma acumulada de las frecuencias relativas.
    dataFrame["Ri"] = dataFrame["ri"].cumsum()

    # Frecuencia relativa porcentual, es la frecuencia relativa multiplicada por 100.
    dataFrame["pi%"] = dataFrame["ri"] * 100

    # Frecuencia acumulada de la frecuencia relativa porcentual, es la suma acumulada de las frecuencias relativas porcentuales.
    dataFrame["Pi%"] = dataFrame["pi%"].cumsum()

    # Mostramos el resultado por consola e informamos a la persona que el contenido se ha añadido en su portapapeles.
    print(dataFrame)
    dataFrame.to_clipboard(excel=True)
    print("El contenido se ha añadido en su portapapeles")
    

#Obtenemos una lista con las edades de las personas en base al archivo leido.

analisis_estadistico(edades)
