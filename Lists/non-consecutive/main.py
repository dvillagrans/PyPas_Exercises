# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(values: list) -> int:
    
    for i in range(len(values) - 1):
      
        if values[i + 1] != values[i] + 1:
            return values[i + 1]  
    return None 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
