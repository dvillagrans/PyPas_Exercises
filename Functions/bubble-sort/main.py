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
