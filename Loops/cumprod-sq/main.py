# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(n: int) -> int:
    
    acum = 1 
    
    for i in range(1, n + 1):  
        acum *= i**2 
        
    return acum  

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    vendor.launch(run)

# Developed by MASG
