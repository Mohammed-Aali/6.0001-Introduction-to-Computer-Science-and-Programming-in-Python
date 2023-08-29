class Cooridnate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def __str__(self):
        return f'<{self.x},{self.y}>'

# conventional way
c = Cooridnate(3,4)
zero = Cooridnate(0,0)
print(c)
print(type(c))
print(type(Cooridnate))

# the conventional way is equivalent to 
# c = Cooridnate(3,4)
# zero = Cooridnate(0,0)
# print(Cooridnate.distance(c, zero))

