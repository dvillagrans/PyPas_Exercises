def run(imoves: str) -> dict:
    movements = imoves.split(',')
    inventory = {}

    for move in movements:
        item = move[0]  
        quantity = int(move[1:])  

        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

    return inventory


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
