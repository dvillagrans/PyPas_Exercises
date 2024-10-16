def run(numbers: list) -> int:
    # Calcular la suma de los opuestos de cada número
    result = sum(-num for num in numbers)
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
