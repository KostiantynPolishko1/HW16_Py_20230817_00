import json
import exception
import os
from pathlib import Path
import menu


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
        f_name = file_rename(f_name)
        with open(f_name, mode) as file:
            print('see new file \'{}\''.format(f_name))
            json.dump(arr_data, file, indent=4)


def list_id(ind: int, arr_data: list, name_fun: str) -> None:
    arr_key = list(dict.keys(arr_data[0]))
    print('\n', name_fun)
    print('   {} {}'.format('N', arr_key[0]))

    for i in range(len(arr_data)):
        if i == ind:
            print("-> {} {}".format((i + 1), arr_data[i][arr_key[0]]))
            continue
        print("   {} {}".format((i + 1), arr_data[i][arr_key[0]]))


def add_data(arr_data: list, name_fun: str) -> None:
    print(name_fun)
    _id = int(input('\tid -> '))
    print('\tcoordinate:')
    x = int(input('\t\tx -> '))
    y = int(input('\t\ty -> '))
    z = int(input('\t\tz -> '))
    _type = input('\t\ttype -> ')
    _name = input('\t\tname -> ')

    arr_data.append({'obj_id': _id, 'pos_x': x, 'pos_y': y, 'pos_z': z, 'obj_type': _type, 'obj_name': _name})


def find_data(arr_data: list, name_fun: str) -> int:

    ind = 0
    while True:
        list_id(ind, arr_data, name_fun)
        ind, operation = menu.receive_pos(len(arr_data) - 1, ind)
        menu.clean_s()

        arr_key = list(dict.keys(arr_data[ind]))
        if not operation:
            print('data of object:')
            for key in arr_data[ind]:
                print('\t{} -> {}'.format(key, arr_data[ind][key]))

            if menu.exit_menu():
                menu.clean_s()
                return arr_data[ind][arr_key[0]]
            else:
                menu.clean_s()
                continue


def modify_data(arr_data: list, name_fun: str) -> None:
    print(name_fun)


def delete_data(arr_data: list, name_fun: str) -> None:
    print(name_fun)


def get_all_data(arr_data: list, name_fun: str) -> None:
    print(name_fun)
