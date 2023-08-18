import cosmo


if __name__ == '__main__':
    data = cosmo.read_data('data2.json', 'r')
    # cosmo.add_data(data)
    cosmo.save_data('data2.json', 'w', data)

    print(data)
