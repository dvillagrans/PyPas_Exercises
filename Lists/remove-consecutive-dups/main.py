def run(items: list) -> list:
    result = []
    for i in range(len(items)):
        if i == 0 or items[i] != items[i - 1]:
            result.append(items[i])
    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
