def run(text1: str, text2: str) -> str:
    cartesian = ''
    for i in text1:
        for j in text2:
            cartesian += i + j
            
            
            
    return cartesian


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
