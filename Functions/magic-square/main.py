# TODO
def is_magic_square(values):
    if not values:
        return True  
    n = len(values) 
    target_sum = sum(values[0]) 

    for row in values:
        if sum(row) != target_sum:
            return False

    for col in range(n):
        if sum(values[row][col] for row in range(n)) != target_sum:
            return False

    if sum(values[i][i] for i in range(n)) != target_sum:
        return False

    if sum(values[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    return True



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(is_magic_square)
