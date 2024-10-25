# E S C O M  -  I P N
# D A A D
# 4AV1
# Oct 15°, 2024
# @autor: Miguel Alexander Sanchez García
import csv
from pathlib import Path

def run(datafile: Path) -> list:
    data = []

    if isinstance(datafile, str):
        datafile = Path(datafile)

    with datafile.open('r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processed_row = {}
            for key, value in row.items():
                if value == '':
                    processed_row[key] = None
                elif value == 'True':
                    processed_row[key] = True
                elif value == 'False':
                    processed_row[key] = False
                elif value.isdigit():
                    processed_row[key] = int(value)
                else:
                    processed_row[key] = value
            data.append(processed_row)

    return data


if __name__ == '__main__':
    run('data/read_csv/pokemon.csv')

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

# Developed by MASG
