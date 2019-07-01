import random, string, time
from types import DynamicClassAttribute
from enum import Enum


class MyEnum(Enum):

    def __str__(self):
        return self.value

    @DynamicClassAttribute
    def path(self):
        """Class path"""
        return "%s.%s" % (self.__class__.__name__, self.name)


def random_string():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 10)))


def date_now():
    return round(time.time() * 1000)







