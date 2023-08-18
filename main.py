import menu
import cosmo


if __name__ == '__main__':
    ind_menu = 0
    data = cosmo.read_data('data2.json', 'r')

    menu_f = {
        0: ['add_data', cosmo.add_data],
        1: ['find_data', cosmo.find_data],
        2: ['modify_data', cosmo.modify_data],
        3: ['delete_data', cosmo.delete_data],
        4: ['get_all_data', cosmo.get_all_data]
    }

    while True:
        menu.print_menu(ind_menu, menu_f)
        print('\n\t\"w\" - Down, \"s\" - Up: ->', end='')
        ind_menu, operation = menu.receive_pos(len(menu_f)-1, ind_menu)
        menu.clean_s()

        if not operation:
            menu_f[ind_menu][1](data)

    # cosmo.save_data('data2.json', 'w', data)
