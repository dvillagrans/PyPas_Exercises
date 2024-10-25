# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(n: int) -> int:
    
    acum = 1 
    
    for i in range(1, n + 1):  
        acum *= i**2 
        
    return acum  

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)

# Made by DVS
