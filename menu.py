import os
import time


def print_menu(ind: int, menu: dict) -> None:
    print('\nMenu:')
    for i in range(len(menu)):
        if i == ind:
            print('-> {} {}'.format((i + 1), menu[i][0]))
            continue
        print('   {} {}'.format((i + 1), menu[i][0]))


def receive_pos(max_ind: int, ind_pos=0) -> tuple:

    print('\n\t\"w\" - Down, \"s\" - Up: ->', end='')

    min_ind = 0
    while True:
        direct = input(' ')

        # increment & decrement
        if not direct:
            return ind_pos, direct
        elif direct == 'W' or direct == 'w':
            ind_pos += 1
        elif direct == 'S' or direct == 's':
            ind_pos -= 1
        else:
            print('ERROR!')
            print('\n\t\"w\" - Down, \"s\" - Up: ->', end='')
            continue

        # check position
        if ind_pos < min_ind:
            ind_pos = max_ind
        elif ind_pos > max_ind:
            ind_pos = min_ind

        return ind_pos, direct


def clean_s() -> None:
    time.sleep(0)
    os.system('CLS')


def exit_menu() -> bool:
    out_submenu = input('\n\texit -> ')
    if not out_submenu:
        os.system('CLS')
        return True
