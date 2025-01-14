from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculator4
# junta as dependencias
def calculator3_factory():
    numpy_hundler = NumpyHandler()
    calc = Calculator4(numpy_hundler)
    return calc 