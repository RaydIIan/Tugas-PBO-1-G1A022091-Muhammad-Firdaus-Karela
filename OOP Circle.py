class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
my_circle = Circle(5)
print(my_circle.area())
print(my_circle.circumference())
