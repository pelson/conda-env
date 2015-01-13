class CondaEnvException(Exception):
    pass


class NoBinstar(CondaEnvException):
    def __init__(self):
        msg = 'The binstar must be installed to perform this action'
        super(NoBinstar, self).__init__(msg)

class EnvironmentFileNotFound(CondaEnvException):
    def __init__(self, filename, *args, **kwargs):
        msg = '{} file not found'.format(filename)
        self.filename = filename
        super(EnvironmentFileNotFound, self).__init__(msg, *args, **kwargs)
