import os
import json


class FileIsNotError(Exception):
    """appears when not such data file"""
    pass


class FileIsNotReadError(Exception):
    """appears when data file is locked for read"""
    pass


class FileIsNotWriteError(Exception):
    """appears when data file is locked for write"""
    pass


class FileIsNotExecuteError(Exception):
    """appears when data file is locked for execute"""
    pass


def read_data(f_name: str) -> list:
    try:
        if not os.access(f_name, os.F_OK):
            raise FileIsNotError('Data file is absent.')
        elif not os.access(f_name, os.R_OK):
            raise FileIsNotReadError('Data file is locked for read.')
        elif not os.access(f_name, os.W_OK):
            raise FileIsNotWriteError('Data file is locked for write.')
        elif not os.access(f_name, os.X_OK):
            raise FileIsNotExecuteError('Data file is locked for execute.')
    except (FileIsNotError, FileIsNotReadError, FileIsNotWriteError, FileIsNotExecuteError) as ex:
        print(ex)
    finally:
        try:
            with open(f_name, 'r') as file:
                return json.load(file)
        except OSError:
            arr_data = []
            return arr_data
