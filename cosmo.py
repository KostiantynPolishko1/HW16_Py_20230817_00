import json
import exception
import os
from pathlib import Path


def file_rename(f_name) -> str:
    ind = 0
    while True:
        if os.path.exists(f_name):
            ind += 1
            f_name = ('{}—copy({}){}'.format(Path(f_name).stem, ind, Path(f_name).suffix))
            continue
        return f_name


def read_data(f_name: str, mode: str) -> list:
    if exception.check_data(f_name):
        with open(f_name, mode) as file:
            return json.load(file)
    else:
        arr_data = []
        return arr_data


def save_data(f_name: str, mode: str, arr_data: list) -> None:
    if exception.check_data(f_name):
        with open(f_name, mode) as file:
            json.dump(arr_data, file, indent=4)
    else:
        with open(file_rename(f_name), mode) as file:
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
