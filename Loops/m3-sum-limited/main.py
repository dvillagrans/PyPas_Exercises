# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
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

# Hecho por: Miguel Sanchez
