import os


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


def check_data(f_name: str) -> bool:
    try:
        if not os.access(f_name, os.F_OK):
            raise FileIsNotError('Data file is absent.\n')
        elif not os.access(f_name, os.R_OK):
            raise FileIsNotReadError('Data file is locked for read.\n')
        elif not os.access(f_name, os.W_OK):
            raise FileIsNotWriteError('Data file is locked for write.\n')
        elif not os.access(f_name, os.X_OK):
            raise FileIsNotExecuteError('Data file is locked for execute.\n')
    except Exception as ex:
        print(ex)
        return False
    else:
        return True
