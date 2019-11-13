class Point:
    """это класс точки"""
    name = 'Point'
    x = 34
    y = 25

    def __init__(self, x=0, y=0):  # x=0 y=0 тоже можно
        """
        :param x: iks
        :param y: igrik
        """
        self.X = x
        self.Y = y

    def show_attr_class(self):
        print("attr of class x: ", self.__class__.x)
        print("attr of class y: ", self.__class__.y)

    def show_attr_obj(self):
        print("attr of obj x: ", self.x)
        print("attr of obj y: ", self.y)
        print("attr of obj X: ", self.X)
        print("attr of obj Y: ", self.Y)

    # def


pt1 = Point()
pt2 = Point()

#print('-' * 100)
pt1.x = 5
pt1.show_attr_class()
pt1.show_attr_obj()
pt2.show_attr_class()
pt2.show_attr_obj()
print()
Point.x = 5
pt1.show_attr_class()
pt1.show_attr_obj()
pt2.show_attr_class()
pt2.show_attr_obj()
print(Point.__doc__)
help(Point.__init__)
print(Point.__dict__)
print(Point.__bases__)


