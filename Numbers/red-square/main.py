def run(arc_A: float) -> float:
    PI = 3.14
    r = arc_A / (PI / 2)
    area = round(r * r, 10)
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
