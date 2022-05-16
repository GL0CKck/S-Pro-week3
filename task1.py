def fraction_reduction(num, den):
    while num % den != 0:
        old_num = num
        old_den = den

        num = old_den
        den = old_num % old_den
    return den


class MixinFraction:
    @staticmethod
    def add(obj1, obj2):
        new_num = (obj1.num * obj2.den) + (obj2.num * obj1.den)
        new_den = (obj1.den * obj2.den)
        common = fraction_reduction(new_num, new_den)
        new_num = new_num // common
        new_den = new_den // common
        return Fraction(new_num, new_den)

    @staticmethod
    def sub(obj1, obj2):
        new_num = (obj1.num * obj2.den) - (obj2.num * obj1.den)
        new_den = (obj1.den * obj2.den)
        common = fraction_reduction(new_num, new_den)
        new_num = new_num // common
        new_den = new_den // common
        return Fraction(new_num, new_den)

    @staticmethod
    def mul(obj1, obj2):
        new_num = (obj1.num * obj2.num)
        new_den = (obj1.den * obj2.den)
        common = fraction_reduction(new_num, new_den)
        new_num = new_num // common
        new_den = new_den // common
        return Fraction(new_num, new_den)

    @staticmethod
    def truediv(obj1, obj2):
        new_num = (obj1.num * obj2.den)
        new_den = (obj1.den * obj2.num)
        common = fraction_reduction(new_num, new_den)
        new_num = new_num // common
        new_den = new_den // common
        return Fraction(new_num, new_den)


class Fraction(MixinFraction):

    def __init__(self, num, den):

        self.__num = num
        self.__den = den

    @property
    def num(self):
        if isinstance(self.__num, int):
            return self.__num
        else:
            raise ValueError('Value eror')

    @property
    def den(self):
        if isinstance(self.__den, int) and self.__den != 0:
            return self.__den
        else:
            raise ValueError('Value error')

    def __add__(self, obj2):
        new_num = (self.num * obj2.den) + (obj2.num * self.den)
        new_den = (self.num * obj2.den)
        dell = fraction_reduction(new_num, new_den)
        new_num = new_num // dell
        new_den = new_den // dell
        return Fraction(new_num, new_den)

    def __sub__(self, obj2):
        new_num = (self.num * obj2.den) - (obj2.num * self.den)
        new_den = (self.den * obj2.den)
        dell = fraction_reduction(new_num, new_den)
        new_num = new_num // dell
        new_den = new_den // dell
        return Fraction(new_num, new_den)

    def __mul__(self, obj2):
        new_num = (self.num * obj2.num)
        new_den = (self.den * obj2.den)
        dell = fraction_reduction(new_num, new_den)
        new_num = new_num // dell
        new_den = new_den // dell
        return Fraction(new_num, new_den)

    def __truediv__(self, obj2):
        new_num = (self.num * obj2.den)
        new_den = (self.den * obj2.num)
        dell = fraction_reduction(new_num, new_den)
        new_num = new_num // dell
        new_den = new_den // dell
        return Fraction(new_num, new_den)

    def __str__(self):
        return f'{self.__num}/{self.__den}'

    @classmethod
    def str_to_fraction(cls, str_value):
        value = [int(x) for x in str_value.split('/')]

        return cls(*value)


frac1 = Fraction(1, 1)
frac2 = Fraction(3, 1)
frac3 = Fraction.str_to_fraction('3/5')
print(frac3)
print(frac3 + frac1)
print(frac3 - frac1)
print(frac3 * frac2)
print(frac3 / frac2)
print(f'{frac3.num}/{frac3.den}')
print(Fraction.add(frac3, frac1))
print(Fraction.sub(frac3, frac1))
print(Fraction.mul(frac3, frac2))
print(Fraction.truediv(frac3, frac2))

