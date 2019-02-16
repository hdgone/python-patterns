"""
The singleton pattern is a software design pattern that restricts the
instantiation of a class to one. This is useful when exactly one object
is needed to coordinate actions across the system.
"""


class AlreadyDefinedError(BaseException):
    pass


class Singleton:
    """ Singleton class can have the only one instance of itself """

    def __init__(self, _cls):
        self._instances = {}
        self.cls = _cls

        # pass attrs from a base class to the new one
        for name in set(dir(self.cls)) - set(dir(self)):
            setattr(self, name, getattr(self.cls, name))

    def __call__(self, *args, **kwargs):
        if self.cls not in self._instances:
            self._instances[self.cls] = self.cls(*args, **kwargs)
        else:
            raise AlreadyDefinedError(
                "A Singleton instance has been defined already. "
                "You can't have more than 1 Singleton object."
            )
