# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(limit: int) -> None:
    
    suma = 0
    num = 0
    secuencia = []
    
    while suma < limit:
        secuencia.append(num)  
        suma += num  
        num += 3  

    
    for num in secuencia:
        print(num, end=" ") 

    print() 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
