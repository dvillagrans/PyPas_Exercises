# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(input_path: str, output_path: str) -> None:
    # Leer el archivo de entrada
    with open(input_path, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    
    # Procesar las líneas y encontrar palabras comunes
    results = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            words1 = set(lines[i].lower().split())
            words2 = set(lines[j].lower().split())
            common_words = words1.intersection(words2)
            results.append(str(len(common_words)))
    
    # Escribir los resultados en el archivo de salida
    with open(output_path, 'w') as file:
        file.write('\n'.join(results))
        if results:  # Añadir una nueva línea al final solo si hay resultados
            file.write('\n')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
# Developed by MASG
