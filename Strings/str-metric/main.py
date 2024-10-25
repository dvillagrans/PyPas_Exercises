# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(text: str) -> int:
    vocales = 'aeiou'
    metric = 0
    cont_vocales = 0
    caracteres = len(text)
    for i in text:
        if i in vocales:
            cont_vocales+= 1
        
    metric = caracteres*cont_vocales    
    return metric


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
