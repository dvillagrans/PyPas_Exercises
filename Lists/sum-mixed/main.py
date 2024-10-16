def run(items: list) -> int:
    sum_items = sum(int(item) for item in items)
    return sum_items


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
