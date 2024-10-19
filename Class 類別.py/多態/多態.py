"""
演示面向對象的多態特性以及抽象類（接口）的使用

測試修改
"""


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal:Animal):
    """制造點噪音，需要傳入Animal對象"""
    animal.speak()


# 演示多態，使用2個子類對象來調用函數
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 演示抽象類
# 做頂層設計，不直接使用抽象類，而是使用他的具體子類
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制熱"""
        pass

    def swing_l_r(self):
        """左右擺風"""
        pass

# 具體子類
class Midea_AC(AC):
    def cool_wind(self):
        print("美的空調制冷")

    def hot_wind(self):
        print("美的空調制熱")

    def swing_l_r(self):
        print("美的空調左右擺風")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空調制冷")

    def hot_wind(self):
        print("格力空調制熱")

    def swing_l_r(self):
        print("格力空調左右擺風")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()


make_cool(midea_ac)
make_cool(gree_ac)
