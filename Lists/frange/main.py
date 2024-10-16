def run(start: float, stop: float, step: float) -> list:
    values = []

    current = start

    while current < stop:
        values.append(current)
        current += step

    return values

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
