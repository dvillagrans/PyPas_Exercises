# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(html: str) -> str:
    
    titulos = {
        'h1': 1,
        'h2': 2,
        'h3': 3,
        'h4': 4,
        'h5': 5,
        'h6': 6
    }
    
    for titulo, nivel in titulos.items():
        if html.startswith(f"<{titulo}>") and html.endswith(f"</{titulo}>"):
            contenido = html[len(f"<{titulo}>"):-len(f"</{titulo}>")]
            return f"{'#' * nivel} {contenido}"

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
