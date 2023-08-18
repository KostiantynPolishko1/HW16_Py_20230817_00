import menu
import cosmo


if __name__ == '__main__':
    ind_menu = 0
    f_name = 'data.json'
    data = cosmo.read_data(f_name, 'r')

    menu_f = {
        0: ['add_data', cosmo.add_data],
        1: ['find_data', cosmo.find_data],
        2: ['modify_data', cosmo.modify_data],
        3: ['delete_data', cosmo.delete_data],
        4: ['get_all_data', cosmo.get_all_data],
        5: ['exit', cosmo.exit_save]
    }

    while True:
        menu.print_menu(ind_menu, menu_f)
        ind_menu, operation = menu.receive_pos(len(menu_f)-1, ind_menu)
        menu.clean_s()

        if not operation:
            if menu_f[ind_menu][1](data, menu_f[ind_menu][0], f_name):
                print('\tTHE END!')
                break
