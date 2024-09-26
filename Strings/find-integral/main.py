def run(symbol: str) -> str:
    symbol = symbol.split(',')
    integral = f"{int(symbol[0]) // (int(symbol[1]) + 1)}x^{int(symbol[1]) + 1}"
    return integral


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
