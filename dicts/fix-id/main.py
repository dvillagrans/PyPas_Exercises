# Villagran Salazar Diego
# DAD
# Fecha de entrega: 2024/09/27
# Grupo 4AV1
# Fecha: 2024/10/25
def run(db):
    id_mapping = {}
    new_id = 1

    for record in db:
        old_id = record['id']
        id_mapping[old_id] = new_id
        new_id += 1

    for record in db:
        old_id = record['id']
        record['id'] = id_mapping[old_id]

    fixed_db = sorted(db, key=lambda x: x['id'])

    return fixed_db


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Made by DVS
