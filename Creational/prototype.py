from abc import ABC, abstractmethod

import copy

# Abstract Class
class Vehicle(ABC):
    # Constructor:
    def __init__(self,seats, tyres, color, fuel):
        self.seats = seats
        self.tyres = tyres
        self.color = color
        self.fuel = fuel

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass
    
    # Printing objects as per our requirement:
    def __str__(self):
        return f"Seats = {self.seats}\nTyres = {self.tyres}\nColor = {self.color}\nFuel = {self.fuel}"

# Child class:        
class Car(Vehicle):
    
    # Constructor:
    def __init__(self, seats, tyres, color, fuel):
        super().__init__(seats, tyres, color, fuel)

    # Overwritting Cloning Method:
    def clone(self):
        return copy.deepcopy(self)

    
if __name__=="__main__":

    electric_car = Car(5,4, 'White', 'Electric') # Creating Car object
    
    cloned_petrol_car = electric_car.clone() # Clonning Car object
    cloned_petrol_car.fuel = 'Petrol'

    print("Original Car:\n")
    print(electric_car)

    print("\nCloned Petrol car:\n")
    print(cloned_petrol_car)