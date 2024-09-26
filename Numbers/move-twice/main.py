def run(current_pos: int, dice: int) -> int:
    distance = dice * 2
    final_pos = current_pos + distance
    return final_pos


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
