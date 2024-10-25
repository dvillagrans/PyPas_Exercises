# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def is_perfect(n):
    def proper_divisors(num):
        return [i for i in range(1, num) if num % i == 0]
    
    return sum(proper_divisors(n)) == n


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)

# Made by DVS
