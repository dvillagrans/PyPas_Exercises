def run(n: int) -> float:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return run(n - 1) + run(n - 2)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
