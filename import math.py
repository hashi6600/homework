import math

# set pi constant value
# using math module
pi = math.pi

class Wheel:
    # parameterised constructor
    def __init__(self, radius):
        self.radius = radius
        
    # set new radius value
    def swap_radius(self, new_radius):
        self.radius = new_radius
        
    # calculate surface area of wheel
    def wheel_area(self):
        return pi * self.radius * self.radius
        
    # calculate perimeter of wheel
    def wheel_perimeter(self):
        return 2 * pi * self.radius
        
if __name__ == "__main__":
    wheel = Wheel(7)
    morewheels = True
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel: ", wheel.wheel_area())
        print("Perimeter of wheel: ", wheel.wheel_perimeter())
        yn = input("More wheels? Y/N ")
        morewheels = yn == 'y' or yn == 'Y'