"""
The singleton pattern is a software design pattern that restricts the
instantiation of a class to one. This is useful when exactly one object
is needed to coordinate actions across the system.

This solution has been based upon agf's stackoverflow answer:
https://stackoverflow.com/a/6798042/9397534
"""


class AlreadyDefinedError(BaseException):
    pass


class Singleton(type):
    """ Singleton class can have the only one instance of itself """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            raise AlreadyDefinedError(
                "A Singleton instance has been defined already. "
                "You can't have more than 1 Singleton object."
            )
        return cls._instances[cls]
