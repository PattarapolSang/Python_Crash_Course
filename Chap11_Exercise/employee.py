class Employee:
    """Class for storing employee name and salary infos"""

    def __init__(self, first_name, last_name, salary) -> None:
        # Initial attribute #

        self.firstname  = first_name
        self.lastname   = last_name
        self.salary     = salary

    def give_raise(self, increment=5_000):
        # Raising salary #

        self.salary     += increment