# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
from pathlib import Path

def run(route_path: Path) -> tuple:
    route_path = Path(route_path)
    
    distance = 0
    depth = 0
    fuel = 0

    with route_path.open('r', encoding='utf-8') as file:
        fuel = int(file.readline().strip())  # Combustible inicial
        movements = file.readline().strip().split(',')

    for move in movements:
        dx, dy = map(int, move.split(':'))

        # Calcular el costo de combustible antes de aplicar el movimiento
        fuel_cost = 3 * abs(dx) + 2 * abs(dy)
        if fuel < fuel_cost:
            break  # Detener si no hay suficiente combustible

        # Calcular el nuevo estado propuesto
        proposed_new_depth = depth + dy
        proposed_new_distance = distance + dx

        # Verificar y ajustar los límites de profundidad
        if proposed_new_depth < -1:
            break  # Detener si intenta ascender más allá de -1, si eso es permitido
        if proposed_new_depth > 601:
            break  # Detener si intenta descender más allá de 601 metros

        # Aplicar los cambios después de verificar el combustible y los límites
        distance = proposed_new_distance
        depth = proposed_new_depth if proposed_new_depth >= -1 else -1
        fuel -= fuel_cost

    return distance, depth, fuel


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
