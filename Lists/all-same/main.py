def run(items: list) -> bool:
    if not items: 
        return True
    first_item = items[0]
    return all(item == first_item for item in items)


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
