import os
from datetime import datetime
fecha_actual = datetime.now().strftime("%Y/%m/%d")

# Comentarios a insertar al inicio
comentarios_inicio = [
    "# E S C O M  -  I P N",
    "# D A A D",
    "# 4AV1",
    "# Oct 15°, 2024",
    "# @autor: Miguel Alexander Sanchez García"
]

# Comentario a insertar al final
comentario_final = "# Developed by MASG"

# Función para agregar comentarios solo si no están presentes
def agregar_comentarios(file_path):
    with open(file_path, 'r+') as file:
        contenido = file.readlines()

        # Verifica si los comentarios ya están presentes
        if comentarios_inicio[0] in contenido and comentario_final in contenido:
            print(f"Los comentarios ya existen en {file_path}, omitiendo.")
            return

        # Si no están, inserta los comentarios al inicio
        for i, comentario in enumerate(comentarios_inicio):
            contenido.insert(i, comentario + '\n')

        # Inserta el comentario final
        contenido.append('\n' + comentario_final + '\n')

        # Escribe el contenido actualizado
        file.seek(0)
        file.writelines(contenido)

# Función para buscar el archivo main.py y agregar comentarios si no existen
def buscar_main_y_agregar_comentarios(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "main.py":
                file_path = os.path.join(subdir, file)
                print(f"Modificando archivo: {file_path}")
                agregar_comentarios(file_path)

# Directorio donde se ejecuta el script
directorio_raiz = os.getcwd()  # O puedes especificar la ruta manualmente
buscar_main_y_agregar_comentarios(directorio_raiz)
