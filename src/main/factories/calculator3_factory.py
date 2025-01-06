from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3
# junta as dependencias
def calculator3_factory():
    numpy_hundler = NumpyHandler()
    calc = Calculator3(numpy_hundler)
    return calc 