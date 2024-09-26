def run(year: int) -> int:
    if(year % 100 == 0):
        century = year // 100
    else:
        century = year // 100 + 1
    return century


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
