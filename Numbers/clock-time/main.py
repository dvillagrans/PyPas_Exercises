# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
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

# Made by DVS
