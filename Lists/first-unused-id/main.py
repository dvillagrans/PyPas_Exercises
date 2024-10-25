# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(ids: list) -> int:
    
    smallest_unused_id = min(set(range(1, max(ids) + 2)) - set(ids))

    return smallest_unused_id

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
