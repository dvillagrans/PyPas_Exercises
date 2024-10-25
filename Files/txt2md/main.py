# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
def texto_a_markdown_desde_lista(lines: list[str]) -> list[str]:
    markdown_lines = []

    for line in lines:
        # Contar el número de tabuladores al principio de la línea
        level = 0
        while line.startswith('\t'):
            level += 1
            line = line[1:]  # Remover el tabulador inicial para seguir procesando el resto de la línea

        # Crear el encabezado Markdown correspondiente
        header_prefix = '#' * (level + 1)  # Nivel de encabezado en Markdown
        markdown_line = f"{header_prefix} {line.strip()}"  # Remover espacios en blanco al inicio y final
        markdown_lines.append(markdown_line)

    return markdown_lines

# Ejemplo de uso:
input_lines = [
    "Título principal",
    "\tSubtítulo 1",
    "\t\tSubtítulo 1.1",
    "\tSubtítulo 2"
]
markdown_result = texto_a_markdown_desde_lista(input_lines)
print('\n'.join(markdown_result))

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
