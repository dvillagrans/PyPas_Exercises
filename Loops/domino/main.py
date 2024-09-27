def run():
    n = 7
    for i in range(n):
        for j in range(i, n):
            print(f'{i}|{j}', end = ' ')
        print('')


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
