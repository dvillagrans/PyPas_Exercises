# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(values: list) -> int:

    if len(values) < 3:
        return 0
    
    max_val = max(values)
    min_val = min(values)

    tsum = sum(v for v in values if v != max_val and v != min_val)

    return tsum

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
