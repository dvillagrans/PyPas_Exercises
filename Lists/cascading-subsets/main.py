def run(values: list, size: int) -> list:
    
    if not values or size > len(values):
        return []

    cascading = []

    for i in range(len(values) - size + 1):
        cascading.append(values[i:i + size])

    return cascading


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
