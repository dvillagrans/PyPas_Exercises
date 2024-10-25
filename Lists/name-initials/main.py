# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(fullname: str) -> str:
    parts = fullname.split(',')
    surname = parts[0].strip()
    name = parts[1].strip()

    surname_parts = surname.split()
    name_parts = name.split()

    initials = name_parts[0][0].upper() + '.'
    for part in surname_parts:
        initials += part[0].upper() + '.'

    return initials

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
