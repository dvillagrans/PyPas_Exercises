def run(v1: bool, v2: bool) -> bool:
    xor = (v1 and not v2) or (not v1 and v2)
    return xor


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
