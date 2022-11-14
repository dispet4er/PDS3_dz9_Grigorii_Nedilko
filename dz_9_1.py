class Car:
    def __init__(self, make, color, cc):
        self.make = make
        self.color = color
        self.cc = cc

    #additional methods
    def go_forward(self):
        return f"{self.color} {self.make} with {self.cc} motor is going forward"

    def go_backward(self):
        return f"{self.color} {self.make} with {self.cc} motor is going backward"

Car1 = Car("Ford", "Blue", "2000ccm")
Car2 = Car("Honda", "Gray", "1800ccm")
Car3 = Car("Mazda", "White", "2300ccm")
Car4 = Car("Mitsubishi", "Gold", "3000ccm")

print(Car1.color)
print(Car2.cc)
print(Car3.make)
print(Car1.go_backward())
print(f"{Car2.make} has {Car2.cc} cubic capacity and {Car3.make} has {Car3.cc}")

class CarInherited(Car):
    def __init__(self):
        Car.__init__(self, Car1, Car2, Car3)

    def go_right(self):
        return f"{self.color} {self.make} with {self.cc} motor is going right"

    def go_left(self):
        return f"{self.color} {self.make} with {self.cc} motor is going left"

GF_obj = CarInherited()

print(CarInherited.go_left(Car3))
print(CarInherited.go_right(Car4))
print(CarInherited.go_forward(Car1))