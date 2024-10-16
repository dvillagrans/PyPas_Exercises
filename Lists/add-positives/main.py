
def run(numbers: list) -> int:
    
    sum_positive = sum(num for num in numbers if num > 0)

    return sum_positive


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
