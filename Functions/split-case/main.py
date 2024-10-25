# TODO
def split_case(words):
    lower_words = [word for word in words if word.islower()]
    upper_words = [word for word in words if word.isupper()]
    
    return (lower_words, upper_words)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(split_case)
