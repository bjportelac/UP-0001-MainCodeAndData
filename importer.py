from os import path
from pathlib import PurePath

import os
import re
import requests

# Abrir el archivo 'urls.txt' en modo lectura
with open("urls.txt", "r") as fileLinks:
    # Leer todas las líneas del archivo y guardarlas en la lista 'urls'
    urls = fileLinks.readlines()

# Crear una lista 'pureUrls' para almacenar las URL limpias
pureUrls = []
for url in urls:
    # Eliminar los espacios en blanco iniciales y finales de cada URL y agregarla a 'pureUrls'
    pureUrls.append(url.strip())
    print(f"URL Obtenida: {url} \n")

# Crear el directorio donde se guardarán los archivos HTML
directory = "archivos_html"
os.makedirs(directory, exist_ok=True)

# Iterar sobre cada URL en 'pureUrls'
for url in pureUrls:
    # Obtener el nombre del archivo de la URL utilizando 'PurePath'
    file_name = PurePath(url).name

    # Limpiar el nombre del archivo eliminando los caracteres especiales
    clean_filename = re.sub(r"\W+", "", file_name)

    # Combinar el nombre limpio del directorio y  el archivo con la extensión '.html' utilizando 'path.join'
    file_path = os.path.join(directory, clean_filename + ".html")

    print(f"file_name: {file_name} || file_path: {file_path}")
    text = ""

    try:
        # Realizar una solicitud GET a la URL
        response = requests.get(url)
        if response.status_code == 200:
            # Si la respuesta es exitosa (código 200), guardar el contenido en 'text'
            text = response.text
        else:
            # Si hay un error en la respuesta, guardar un mensaje de error en 'text'
            text = f"Error: {response.status_code} - {response.reason}"
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exception:
        # Capturar excepciones de conexión o tiempo de espera y mostrar un mensaje de error
        print(f"Ha ocurrido un error: {exception}")

    # Escribir el contenido en el archivo especificado por 'file_path'
    with open(file_path, "w") as fileWriter:
        fileWriter.write(text)

    print(f"Archivo escrito con éxito en: {file_path}")

