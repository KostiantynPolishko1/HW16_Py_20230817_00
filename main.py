import json
import cosmo
# Task1 cosmo objects

if __name__ == '__main__':
    data = cosmo.read_data()
    cosmo.add_data(data)
    cosmo.save_data(data)

    print('\nEND')
