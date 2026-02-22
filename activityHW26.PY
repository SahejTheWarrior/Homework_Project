class Dog:
    # Class variable
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def details(self):
        return f"Animal: {Dog.animal}, Breed: {self.breed}, Colour: {self.colour}"


# Creating two dog objects
dog1 = Dog("Labrador", "Golden")
dog2 = Dog("German Shepherd", "Black and Tan")

print(dog1.details())
print(dog2.details())
