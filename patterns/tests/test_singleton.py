import pytest

from patterns.decorators.singleton import Singleton as Singleton_dec,\
    AlreadyDefinedError as DecoratorException
from patterns.meta.singleton import Singleton,\
    AlreadyDefinedError as MetaclassException


@Singleton_dec
class Boss:
    def __init__(self, name):
        self.name = name


class Owner(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


def test_decorator_creating_more_than_one_singleton_instance_fails():
    with pytest.raises(DecoratorException):
        boss1 = Boss(name='John')
        boss2 = Boss(name='Jack')


def test_metaclass_creating_more_than_one_singleton_instance_fails():
    with pytest.raises(MetaclassException):
        owner1 = Owner(name='John')
        owner2 = Owner(name='Jack')
