def run(nums_dups: list) -> list:
    nums_unique = []
    seen = set()
    for num in nums_dups:
        if num not in seen:
            nums_unique.append(num)
            seen.add(num)
    return nums_unique


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
