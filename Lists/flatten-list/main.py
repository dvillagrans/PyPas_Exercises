# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(elements: list) -> list:
    flatten_elements = []
    for element in elements:
        if isinstance(element, list):  
            flatten_elements.extend(element)
        else:
            flatten_elements.append(element)
    return flatten_elements

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
