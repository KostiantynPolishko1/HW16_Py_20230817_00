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


def list_id(ind: int, arr_data: list, name_fun: str) -> None:
    arr_key = list(dict.keys(arr_data[0]))
    print('\n', name_fun)
    print('   {} {}'.format('N', arr_key[0]))

    for i in range(len(arr_data)):
        if i == ind:
            print("-> {} {}".format((i + 1), arr_data[i][arr_key[0]]))
            continue
        print("   {} {}".format((i + 1), arr_data[i][arr_key[0]]))


def add_data(arr_data: list, name_fun: str, f_name='') -> bool:
    while True:
        print(name_fun)
        _id = int(input('\tid -> '))
        print('\tcoordinate:')
        x = int(input('\t\tx -> '))
        y = int(input('\t\ty -> '))
        z = int(input('\t\tz -> '))
        _type = input('\t\ttype -> ')
        _name = input('\t\tname -> ')

        arr_data.append({'obj_id': _id, 'pos_x': x, 'pos_y': y, 'pos_z': z, 'obj_type': _type, 'obj_name': _name})

        if menu.exit_menu():
            return False
        else:
            menu.clean_s()
            continue


def find_data(arr_data: list, name_fun: str, function='') -> int:

    ind = 0
    while True:
        list_id(ind, arr_data, name_fun)
        ind, operation = menu.receive_pos(len(arr_data) - 1, ind)
        menu.clean_s()

        if not operation:
            print('data of object:')
            for key in arr_data[ind]:
                print('\t{} -> {}'.format(key, arr_data[ind][key]))

            if function == 'delete_data':
                return ind
            else:
                if menu.exit_menu():
                    return 0
                else:
                    menu.clean_s()
                    continue


def modify_data(arr_data: list, name_fun: str, f_name='') -> bool:
    print(name_fun)
    return False


def delete_data(arr_data: list, name_fun: str, f_name='') -> bool:

    while True:
        ind = find_data(arr_data, name_fun, 'delete_data')
        del_element = input('\n\tdel object -> ')
        if not del_element:
            del arr_data[ind]
            menu.clean_s()
            return False
        menu.clean_s()


def get_all_data(arr_data: list, name_fun: str, f_name='') -> bool:
    print(name_fun)
    return False


def exit_save(arr_data: list, name_fun: str, f_name) -> bool:
    print('\n\t', name_fun)

    def save_data(_f_name: str, _arr_data: list, mode='w') -> None:
        if exception.check_data(_f_name):
            with open(_f_name, mode) as file:
                json.dump(_arr_data, file, indent=4)
        else:
            _f_name = file_rename(_f_name)
            with open(_f_name, mode) as file:
                print('see new file \'{}\''.format(_f_name))
                json.dump(_arr_data, file, indent=4)

    save_data(f_name, arr_data, 'w')
    return True
