# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(n: int) -> int:
    
    digit = str(n)
    if digit[0] == '-':
        digit = digit[1:]
        
    
    
    leng= len(digit)
    
    result = n * 5 ** leng

    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
