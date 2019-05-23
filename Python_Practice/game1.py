"""
凹凸曼打小怪兽
"""
from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""
    # 通过__slots__魔法限定对象可以绑定的成员对象
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化方法
        :param name:名字
        :param hp:生命值
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other:被攻击的对象
        :return:
        """
        pass


class Ultraman(Fighter):
    """凹凸曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        初始化方法
        :param name:姓名
        :param hp:生命值
        :param mp:魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
        究极必杀技：打掉对方50滴血或者3/4血量
        :param other:被攻击的对象
        :return:使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """
        魔法攻击
        :param other:被攻击的群体
        :return:使用成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s凹凸曼~~~\n' % self._name + '生命值：%d\n' % self._hp + '魔法值:%d\n' % self._mp


class Monster(Fighter):
    """小怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽\n' % self._name + '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽活着"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选择一直活着的怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    """显示凹凸曼和小怪兽信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end=' ')


def main():
    u = Ultraman('迪迦', 1000, 120)
    m1 = Monster('哥斯拉', 250)
    m2 = Monster('肯尼', 500)
    m3 = Monster('猪头', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('======第%02d回合======' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n======游戏结束======\n')
    if u.alive > 0:
        print('%s凹凸曼获胜！' % u.name)
    else:
        print('小怪兽获胜')


if __name__ == '__main__':
    main()

"""
代码简单，工整，一目了然
学习记录：一个简单的游戏，但是编写的很工整很一目连然，这是需要掌握的基础，自己还没有掌握，多读多写自己动手
游戏想法：双发普通攻击的伤害值随机，技能的释放是随机的，可以将技能的释放改为玩家控制，增加可玩性，
    其次是随机出现miss伤害，怪物出现随机大招（放大招之前会有提醒，凹凸曼可使用格挡（格挡存在释放次数））...
"""
