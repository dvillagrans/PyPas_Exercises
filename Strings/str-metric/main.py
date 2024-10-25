# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(text: str) -> int:
    vocales = 'aeiou'
    metric = 0
    cont_vocales = 0
    caracteres = len(text)
    for i in text:
        if i in vocales:
            cont_vocales+= 1
        
    metric = caracteres*cont_vocales    
    return metric


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
