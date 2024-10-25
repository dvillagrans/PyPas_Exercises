# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def run(smb_path: str) -> tuple:
    smb_path.startswith('//')
    parts = smb_path[2:].split('/', 1)
    host = parts[0]
    path = '/' + parts[1] if len(parts) > 1 else ''
    return host, path


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
