def run(lst, item):
    if item in lst:
        if lst.index(item) == len(lst) - 1:
            return None
        else:
            return lst[lst.index(item) + 1]
    else:
        return None
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
