# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(key1: str, key2: str, key3: str) -> str:
    action = ""
    key1 = key1.lower()
    key2 = key2.lower()
    key3 = key3.lower()
    if key1 == "ctrl" and key2 == "alt" and key3 == "t":
        action = "Open terminal"
    elif key1 == "ctrl" and key2 == "alt" and key3 == "l":
        action = "Lock screen"
    elif key1 == "ctrl" and key2 == "alt" and key3 == "d":
        action = "Show desktop"
    elif key1 == "alt" and key2 == "f2" and key3 == "":
        action = "Run console"
    elif key1 == "ctrl" and key2 == "q" and key3 == "":
        action = "Close window"
    elif key1 == "ctrl" and key2 == "alt" and key3 == "del":
        action = "Log out"
    else:
        action = "Undefined"
    return action


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
