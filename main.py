import cosmo
import exception


if __name__ == '__main__':
    data = exception.read_data('data.json')
    # cosmo.add_data(data)
    # cosmo.save_data(data)

    print(data)
