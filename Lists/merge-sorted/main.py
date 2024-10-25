# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García

def run(values1: list, values2: list) -> list:
    i, j = 0, 0
    merged = []
        
    while i < len(values1) and j < len(values2):
        
        if values1[i] < values2[j]:
            if not merged or values1[i] != merged[-1]:
                merged.append(values1[i])
            i += 1
        elif values1[i] > values2[j]:
            if not merged or values2[j] != merged[-1]:
                merged.append(values2[j])
            j += 1
        else:  
            if not merged or values1[i] != merged[-1]:
                merged.append(values1[i])
            i += 1
            j += 1
    
    while i < len(values1):
        if not merged or values1[i] != merged[-1]:
            merged.append(values1[i])
        i += 1
   
    while j < len(values2):
        if not merged or values2[j] != merged[-1]:
            merged.append(values2[j])
        j += 1

    return merged


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
