import pytest
from faker import Faker

faker = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int)

def pytest_generate_tests(metafunc):
    num_records = metafunc.config.getoption("num_records")
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames and "operation" in metafunc.fixturenames:
        metafunc.parametrize(
            "a, b, operation", 
            [(faker.random_number(), faker.random_number(), 
              faker.random_element(elements=('add', 'subtract', 'multiply', 'divide'))) 
             for _ in range(num_records)]
        )
