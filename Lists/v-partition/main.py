# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
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

# Hecho por: Miguel Sanchez
