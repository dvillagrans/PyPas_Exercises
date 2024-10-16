# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(formula: list) -> bool:
    # Rule 1: Component 1 and Component 2 cannot both be selected.
    if 1 in formula and 2 in formula:
        return False

    # Rule 2: Component 3 and Component 4 cannot both be selected.
    if 3 in formula and 4 in formula:
        return False

    # Rule 3: Component 5 and Component 6 cannot both be selected.
    if 5 in formula and 6 in formula:
        return False

    # Rule 4: At least one of Component 7 or Component 8 must be selected.
    if 7 not in formula and 8 not in formula:
        return False

    # If none of the rules are violated, the formula is valid.
    return True

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
