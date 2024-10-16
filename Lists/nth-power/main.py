def run(values: list, power: int) -> int:
    
    if power < 0 or power >= len(values):
        return -1
    
    element = values[power]
    result = element ** power

    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
