# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
# TODO
def consecutive_seq(items, target_count, index=0, current_count=1):
    if index + 1 >= len(items):
        return items[index] if current_count >= target_count else False
    
    if items[index] == items[index + 1]:
        current_count += 1
    else:
        if current_count >= target_count:
            return items[index]
        current_count = 1
    
    result = consecutive_seq(items, target_count, index + 1, current_count)
    if result:
        return result
    
    return False



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(consecutive_seq)

# Made by DVS
