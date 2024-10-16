def run(number: int) -> list:
    
    reversed_str = str(number)[::-1]
    
    rev_digits = [int(char) for char in reversed_str]
    return rev_digits

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
