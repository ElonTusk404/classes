"""Create a class hierarchy that represents different types of vehicles. Start with a base class called "Vehicle" and create two subclasses: "Car" and "Motorcycle." Each class should have appropriate attributes and methods based on their specific characteristics.

1. Base class: Vehicle
   - Attributes:
     - make: The make or manufacturer of the vehicle.
     - model: The model of the vehicle.
     - year: The manufacturing year of the vehicle.
   - Methods:
     - start(): Prints a message indicating that the vehicle has started.
     - stop(): Prints a message indicating that the vehicle has stopped.

2. Subclass: Car (inherits from Vehicle)
   - Additional Attributes:
     - num_doors: The number of doors the car has.
     - num_seats: The number of seats available in the car.
   - Additional Methods:
     - honk(): Prints a message indicating that the car is honking.

3. Subclass: Motorcycle (inherits from Vehicle)
   - Additional Attributes:
     - is_sport: A boolean value indicating whether the motorcycle is a sport bike or not.
   - Additional Methods:
     - wheelie(): Prints a message indicating that the motorcycle is performing a wheelie.

Create instances of the Car and Motorcycle classes, and call their respective methods to demonstrate the inheritance and unique behavior of each subclass. Experiment with different attributes and methods to further explore the concept of inheritance.

This task will allow students to practice creating a class hierarchy, utilizing inheritance to reuse code from the base class, and adding specific characteristics to the subclasses. It encourages students to think about the relationship between different types of vehicles and how they can inherit common behavior from a base class while having their unique features.

Happy coding and have fun with the task!"""

class Vehicle:
    def __init__(self, make, model, year) -> None :
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print(f"{self.title} has started.")
    def stop(self):
        print(f"{self.model} has stopped.")
    
class Car(Vehicle):

    def __init__(self, make, model, year, num_doors, num_seats) -> None:
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.num_seats = num_seats
    
    def honk(self):
        print(f"{self.model} is honking.")

class Motocycle(Vehicle):

    def __init__(self, make, model, year, is_sport: bool) -> None:
        super().__init__(make, model, year)
        self.is_sport = is_sport

    def wheelie(self):
        print(f"The {self.model} is performing a wheelie.")
