import json


def read_data() -> list:
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except:
        arr_data = []
        return arr_data


def save_data(arr_data: list) -> None:
    with open('data.json', 'w') as file:
        json.dump(arr_data, file, indent=4)


def add_data(arr_data: list) -> None:
    print('data of cosmo object')
    _id = int(input('\tid -> '))
    print('\tcoordinate:')
    x = int(input('\t\tx -> '))
    y = int(input('\t\ty -> '))
    z = int(input('\t\tz -> '))
    _type = input('\t\ttype -> ')
    _name = input('\t\tname -> ')

    arr_data.append({'obj_id': _id, 'pos_x': x, 'pos_y': y, 'pos_z': z, 'obj_type': _type, 'obj_name': _name})
