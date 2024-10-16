def run(items: dict) -> bool:
    
    values = list(items.values())
    
    all_same = all(value == values[0] for value in values) if values else True

    return all_same


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
