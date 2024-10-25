# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(age: int, weight: int, heartbeat: int, platelets: int) -> bool:
    suitable_for_donation = False
    if (18 <= age <= 65) and (50 <= weight) and (50 <= heartbeat <= 110) and (150000 <= platelets):
        suitable_for_donation = True
    return suitable_for_donation


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
