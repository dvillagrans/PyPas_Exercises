# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
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

# Hecho por: Miguel Sanchez
