# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
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

# Developed by MASG
