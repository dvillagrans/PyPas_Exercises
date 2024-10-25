# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
