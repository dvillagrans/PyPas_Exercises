# E S C O M  -  I P N
# D A A D
# 4AV1
# 2024/10/16
# @autor: Miguel Alexander Sanchez García
def run(hours: int, minutes: int, seconds: int) -> float:
    hours_in_milliseconds = hours * 60 * 60 * 1000
    minutes_in_milliseconds = minutes * 60 * 1000
    seconds_in_milliseconds = seconds * 1000
    time_since_midnight = hours_in_milliseconds + minutes_in_milliseconds + seconds_in_milliseconds
    return time_since_midnight


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Hecho por: Miguel Sanchez
