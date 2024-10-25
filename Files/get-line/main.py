# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path # type: ignore


def run(input_path: Path, line_no: int) -> str:
    if not isinstance(input_path, Path):
        input_path = Path(input_path)

    # Verificamos que el número de linea sea valido
    if line_no < 1:
        return None

    try:
        # Abrimos el archivo y leemos hasta encontrar la linea deseada
        with input_path.open('r', encoding='utf-8') as file:
            for current_line, line in enumerate(file, start=1):
                if current_line == line_no:
                    return line.strip()
            # Si terminamos de leer el archivo sin encontrar la linea, devolvemos None
            return None
    except FileNotFoundError:
        print(f"El archivo {input_path} no existe.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
