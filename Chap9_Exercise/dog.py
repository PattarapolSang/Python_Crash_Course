class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age) -> None:
        """Initial name and age attribute"""
        self.name   = name
        self.age    = age
    
    def sit(self):
        """Simulate dog sitting behavior to command prompt"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate dog roll over behavior to command prompt"""
        print(f"{self.name} is now rolling over the ground")

class Restaurant:
    """A simple class for storing the restaurant information"""

    def __init__(self, name, cuisine) -> None:
        """Initial name and cuisine"""
        self.name       = name
        self.cuisine    = cuisine

    def describe_restaurant(self):
        """Print the information of the restaurant"""
        print(f"This is the '{self.name}'. The {self.cuisine}.")

    def open_restaurant(self):
        """Print message for opening the restaurant"""
        print(f"Now '{self.name} is opened!!")


my_dog      = Dog('Willy', 6)
your_dog    = Dog('Sam', 2)

print(f"My dog's name is {my_dog.name}")
print(f"His age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}")
print(f"His age is {your_dog.age}")
your_dog.sit()
your_dog.roll_over()

print('\n')

my_restaurant   = Restaurant('KFC', 'Fast food')
restaurant_1    = Restaurant('Mcdonald', 'Fast')
restaurant_2    = Restaurant('Fai', 'Thai')

print(f'My restaurant name is {my_restaurant.name}, the {my_restaurant.cuisine}')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant_1.describe_restaurant()
restaurant_2.open_restaurant()

print('\n')
