# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(values: list, ref_value: int) -> list:
    # Create two sublists: one for values less than ref_value, and one for greater or equal values
    less_than_ref = [value for value in values if value < ref_value]
    greater_or_equal_ref = [value for value in values if value >= ref_value]

    # Return the combined list containing both sublists
    return [less_than_ref, greater_or_equal_ref]

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
