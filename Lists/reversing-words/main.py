def run(text: str) -> str:
    
    words = text.split()
    
    reversing = ' '.join(words[::-1]).lower()

    return reversing


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
