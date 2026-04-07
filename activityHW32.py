class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"


# Polymorphism in action
def car_details(car):
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print("-" * 30)


# Creating objects
bmw = BMW()
ferrari = Ferrari()

# Using polymorphism
car_details(bmw)
car_details(ferrari)