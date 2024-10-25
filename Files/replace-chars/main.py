# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path

def run(input_path: Path, replacements: str, output_path: Path) -> bool:
    input_path = Path(input_path)
    output_path = Path(output_path)
    expected_path = output_path.with_suffix('.expected')

    # Construir un diccionario de reemplazos a partir del string 'a|b|c|d' -> {'a': 'b', 'c': 'd'}
    replacement_dict = {pair[0]: pair[1] for pair in replacements.split('|')}

    try:
        # Leer y procesar el archivo de entrada, luego escribir el archivo de salida
        with input_path.open('r', encoding='utf-8') as infile, \
             output_path.open('w', encoding='utf-8', newline='\n') as outfile:
            for line in infile:
                for old_char, new_char in replacement_dict.items():
                    line = line.replace(old_char, new_char)
                outfile.write(line.rstrip() + '\n')

    except FileNotFoundError:
        print(f"El archivo {input_path} no existe.")
        return False
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return False

    # Comparar el archivo generado con el archivo esperado
    if expected_path.exists():
        try:
            with output_path.open('r', encoding='utf-8') as gen_file, \
                 expected_path.open('r', encoding='utf-8') as exp_file:
                generated_lines = gen_file.readlines()
                expected_lines = exp_file.readlines()

            # Normalizar contenido (remover espacios y saltos de línea al final)
            generated_lines = [line.strip() for line in generated_lines]
            expected_lines = [line.strip() for line in expected_lines]

            # Comparar contenido normalizado
            return generated_lines == expected_lines

        except FileNotFoundError:
            print(f"El archivo {expected_path} no existe.")
            return False

    return False

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
