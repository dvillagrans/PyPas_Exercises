# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
# TODO
def bsort(items):
    sorted_items = items[:]
    n = len(sorted_items)
    
    for i in range(n):
        swapped = False
        
        for j in range(1, n - i):
            if sorted_items[j - 1] > sorted_items[j]:
                sorted_items[j - 1], sorted_items[j] = sorted_items[j], sorted_items[j - 1]
                swapped = True
        
        if not swapped:
            break
    
    return sorted_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(bsort)

# Developed by MASG
