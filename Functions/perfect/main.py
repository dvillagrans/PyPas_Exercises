# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO
def is_perfect(n):
    def proper_divisors(num):
        return [i for i in range(1, num) if num % i == 0]
    
    return sum(proper_divisors(n)) == n


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_perfect)

# Developed by MASG
