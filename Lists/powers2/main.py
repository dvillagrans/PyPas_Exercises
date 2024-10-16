def run(num_powers: int) -> list:
    
    powers2 = [2 ** i for i in range(num_powers + 1)]

    return powers2

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
