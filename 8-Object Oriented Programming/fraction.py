class Fraction(object):
    def __init__(self, num, denum):
        """num and denum are integers"""
        assert type(num) == int and type(denum) == int
        self.num = num
        self.denum = denum
    def __str__(self):
        """Returns a string representation of self """
        return str(self.num) + '/' + str(self.denum)
    def __add__(self, other):
        """Returns a new fraction representing adding two fractions"""
        top = self.num * other.denum + self.denum* other.num
        bottom = self.denum * other.denum
        return Fraction(top, bottom)
    def __sub__(self, other):
        """Returns a new fraction represinting substracting two fractions"""
        top = self.num * other.denum - self.denum * other.num
        bottom = self.denum * other.denum
        return Fraction(top, bottom)
    def __float__(self):
        """Returns a float value of the fraction"""
        return self.num/self.denum
    def inverse(self):
        """Returns a new fraction representing the inverse of the fraction"""
        return Fraction(self.denum, self.num)

a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b # c is a fraction object
print(c)
print(float(c))
print(float(b.inverse()))