"""
继承和多态
继承：一个类从另一个类中将属性和方法继承下来
多态：通过方法重写我们可以让父类的行为在子类中拥有不同的实现版本
    Python从语法层面并没有像Java或C#那样提供对抽象类的支持，
    但是我们可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果
所谓抽象类就是不能够创建对象的类
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s:汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s:喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
