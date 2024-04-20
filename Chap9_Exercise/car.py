class Car:
    """A simple attempt to represent the car"""

    def __init__(self, maker, model, year) -> None:
        """Initial attributes maker, model, year"""
        self.maker  = maker
        self.model  = model
        self.year   = year
        self.odometer   = 0
    
    def descriptive_name(self):
        """Return the description of overall this car"""
        long_name   = f'{self.maker} {self.model} {self.year}'
        return long_name
    
    def read_odometer(self):
        """Print the odometer reading"""
        print(f"This car's odometer is {self.odometer}")

    def update_odometer(self, mileage):
        """
        Update the car's odometer
        [REJECT if update value is less than the current value]
        """
        if mileage < self.odometer:
            print("Cannot update the mileage due to the update value is less than the current")
        else:
            self.odometer   = mileage

    def increment_odometer(self, increment):
        """"
        Increase the mileage with the input value
        [Cannot input < 0]
        """
        if increment < 0:
            print("Cannot update negative value")
        else:
            self.odometer += increment

    def fill_gas_tank(self):
        print("Please fill the gas tank")

class Battery:

    def __init__(self, battery_size = 40) -> None:
        self.battery_size   = battery_size

    def describe_battery_size(self):
        print(f"This electric car have {self.battery_size} kWH.")

    def get_range(self):
        if self.battery_size > 40:
            range   = 150
        else:
            range   = 220
        
        print(f"This electric car has range {range} km.")

class ElectricCar(Car):

    def __init__(self, maker, model, year) -> None:
        super().__init__(maker, model, year)
        self.battery        = Battery(60)

    def fill_gas_tank(self):
        print("Electric car does not has a gas tank")

    
my_car  =   Car('Audi', 'A4', 2024)
print(my_car.descriptive_name())
my_car.read_odometer()

my_car.odometer = 23
my_car.read_odometer()

my_car.update_odometer(40)
my_car.read_odometer()

my_car.update_odometer(20)
my_car.read_odometer()

my_car.update_odometer(60)
my_car.read_odometer()

my_car.increment_odometer(-3)
my_car.increment_odometer(50)
my_car.read_odometer()

print('\n')

my_leaf = ElectricCar('Nissan', 'Leaf', '2019')
print(my_leaf.descriptive_name())
# my_leaf.describe_battery_size()

my_car.fill_gas_tank()
my_leaf.fill_gas_tank()

my_leaf.battery.describe_battery_size()
my_leaf.battery.get_range()