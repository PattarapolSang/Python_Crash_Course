import pytest
from employee import Employee

@pytest.fixture
def employee_function():
    employee1   = Employee('Pattarapol', 'Sangaroon', 10_000)
    return employee1

def test_increment_default(employee_function):
    employee_function.give_raise()
    assert employee_function.salary == (10_000 + 5_000)

def test_increment_random(employee_function):
    employee_function.give_raise(10_000)
    assert employee_function.salary == (10_000 + 10_000)