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
