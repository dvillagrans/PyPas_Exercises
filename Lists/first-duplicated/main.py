# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(values: list) -> int:
    seen = set()  # A set to keep track of seen values

    for value in values:
        if value in seen:
            return value  # Return the first duplicate we find
        seen.add(value)

    return None  # If no duplicates are found, return None

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
