# TODO
def rslice(texto, wsize):
    if not texto:
        return []

    return [texto[:wsize]] + rslice(texto[wsize:], wsize)

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(rslice)
