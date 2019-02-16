"""
The singleton pattern is a software design pattern that restricts the
instantiation of a class to one. This is useful when exactly one object
is needed to coordinate actions across the system.

https://stackoverflow.com/a/6798042/9397534
"""


from functools import wraps


class AlreadyDefinedError(BaseException):
    pass


def singleton(cls):
    """ Singleton class can have the only one instance of itself """

    _instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        else:
            raise AlreadyDefinedError(
                "A Singleton instance has been defined already. "
                "You can't have more than 1 Singleton object."
            )

        return _instances[cls]

    _instances = {}
    return wrapper
