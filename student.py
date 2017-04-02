from __future__ import print_function


class Student:

    def __init__(self, name, chinese, math, english):
        self.name = name
        self.english = english
        self.math = math
        self.chinese = chinese

    def get_sum(self):
        return self.chinese + self.english + self.math

    def get_avg(self):
        return self.get_sum() / 3

    def __str__(self):
        return "{0} (name: {1} sum: {2} avg: {3})".format(self.__class__.__name__,
                                                          self.name,
                                                          self.get_sum(),
                                                          self.get_avg())


