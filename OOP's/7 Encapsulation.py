# Encapsulation refers to the principle of bundling data (attributes) and
# methods (functions that operate on the data) together within a class.
# It allows us to restrict direct access to some of the object's components and
# hide the internal state and implementation details from the outside world.

class Car:
    def __init__(self, brand, model):
        self.brand = brand    # Public attribute
        self.__model = model  # Private attribute

    def get_model(self):    #Getter method
        return self.__model

    def set_model(self, new_model):
        # Perform validation or other checks before setting
        self.__model = new_model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)      # Accessing public attribute directly
# print(my_car.__model)  # This would raise an AttributeError because __model is private
print(my_car.get_model())   # Accessing private attribute via getter method
my_car.set_model("Camry")   # Modifying private attribute via setter method
