import os
import re
from bs4 import BeautifulSoup

# Directorio que contiene los archivos HTML
directory = "archivos_html"

# Obtener la lista de archivos en el directorio
file_list = os.listdir(directory)

# Diccionario para almacenar los resultados
parsed_dict = {}

# Iterar sobre los archivos en el directorio
for file_name in file_list:
    # Combinar la ruta del directorio con el nombre de archivo
    file_path = os.path.join(directory, file_name)
    
    # Verificar si el elemento en el directorio es un archivo
    if os.path.isfile(file_path):
        # Abrir el archivo y realizar las operaciones deseadas
        with open(file_path, 'r') as file:
            # Leer el contenido del archivo
            content = file.read()

            # Imprimir información del archivo actual
            print(f"Examinando el Archivo: {file_name}\n")

            # Crear el objeto BeautifulSoup
            soup = BeautifulSoup(content, "html.parser")

            # Encontrar todos los elementos <p>
            paragraphs = soup.find_all('p')

            # Obtener los textos de los párrafos
            paragraphs_text = []
            for p in paragraphs:
                paragraphs_text.append(p.text)

            # Agregar la lista de párrafos al diccionario
            parsed_dict[file_name] = paragraphs_text

# Nombre del archivo de salida
output_file = "resultado.txt"

# Guardar el diccionario en un archivo de texto
with open(output_file, "w") as file:
    for file_name, paragraphs in parsed_dict.items():
        file.write(f"Archivo: {file_name}\n")
        file.write("Contenido:\n")
       
        # Escribir cada párrafo en el archivo de salida
        for paragraph in paragraphs:
            # Eliminar caracteres no alfanuméricos utilizando expresiones regulares
            paragraph = re.sub(r"\W+", " ", paragraph)
            file.write(f"{paragraph}\n")
        file.write("-----------------------------\n")

# Imprimir mensaje de confirmación
print(f"El diccionario se ha guardado en el archivo: '{output_file}'.")
