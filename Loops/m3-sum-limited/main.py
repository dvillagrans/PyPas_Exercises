# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
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

# Developed by MASG
