# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
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

# Made by DVS
