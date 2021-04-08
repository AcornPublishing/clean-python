from abc import ABCMeta, abstractmethod

class Fruit(metaclass=ABCMeta):

    @abstractmethod
    def taste(self):
        pass

    @abstractmethod
    def originated(self):
        pass


class Apple:
    def originated(self):
        return "Central Asia"


fruit = Fruit()
"""
TypeError:
"Can't instantiate abstract class Fruit with abstract methods originated, taste"
"""
