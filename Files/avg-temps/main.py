# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path

def run(input_path: Path, output_path: Path) -> bool:
    # Asegurarse de que input_path y output_path sean objetos de tipo Path
    input_path = Path(input_path)
    output_path = Path(output_path)

    # Leer el archivo de entrada
    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.readlines()

    monthly_averages = []

    # Calcular la temperatura media de cada mes
    for line in data:
        temps = line.strip().split(',')
        temps = [float(temp) for temp in temps if temp.strip()]
        if temps:  # Asegurarse de que no esté vacío
            average = sum(temps) / len(temps)
            monthly_averages.append(f"{average:.2f}")

    # Escribir el archivo de salida con los promedios calculados
    with open(output_path, 'w', encoding='utf-8', newline='\n') as file:
        file.write('\n'.join(monthly_averages) + '\n')

    # Verificar si el archivo esperado está disponible y comparar si existe
    expected_path = output_path.with_suffix('.expected')
    if expected_path.exists():
        with open(output_path, 'r', encoding='utf-8') as gen_file:
            generated = gen_file.read().strip()
        with open(expected_path, 'r', encoding='utf-8') as exp_file:
            expected = exp_file.read().strip()

        return generated == expected

    return True

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
