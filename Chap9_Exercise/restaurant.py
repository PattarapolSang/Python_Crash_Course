class Restaurant:
    """A simple class for storing the restaurant information"""

    def __init__(self, name, cuisine) -> None:
        """Initial name and cuisine"""
        self.name       = name
        self.cuisine    = cuisine
        self.number_served  = 0

    def describe_restaurant(self):
        """Print the information of the restaurant"""
        print(f"This is the '{self.name}'. The {self.cuisine}.")

    def open_restaurant(self):
        """Print message for opening the restaurant"""
        print(f"Now '{self.name} is opened!!")

    def check_served_number(self):
        """Print the served number this restaurant has served"""
        print(f"Now this {self.name} has served {self.number_served} customers")

    def set_number_served(self, served):
        """Set the new number that this restaurant has served"""
        self.number_served  = served

    def increase_number_served(self, increase):
        """
        Increase the number of serve
        [Must be positive value]
        """
        if increase > 0:
            self.number_served += increase
        else:
            print("The input must be positive value!!!")

class IceCreamStand(Restaurant):
    """
    A child class for the Ice cream stand specific restaurant
    """

    def __init__(self, name, cuisine, flavours = ['vanilla', 'chocolate']) -> None:
        """"Initialize by restaurant class with super() function"""
        super().__init__(name, cuisine)
        self.flavors = flavours

    def display_flavour(self):
        """"Display the flavour"""
        print("Flavours available:")
        for flavour in self.flavors:
            print(f"\t{flavour}")


# my_restaurant   = Restaurant('KFC', 'Fast food')

# my_restaurant.check_served_number()
# my_restaurant.number_served     = 10
# my_restaurant.check_served_number()

# my_restaurant.set_number_served(50)
# my_restaurant.check_served_number()

# my_restaurant.increase_number_served(-3)
# my_restaurant.increase_number_served(50)
# my_restaurant.check_served_number()
# print('\n')

# my_icecream     = IceCreamStand('Baskin', 'Ice cream', ['Chocolate', 'Cookie&Cream', 'Strawberry'])
# my_icecream.display_flavour()
# my_icecream.describe_restaurant()