from pytest import raises
from src.calculators.calculator_4 import Calculator4
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict, List

# Mock para simular a requisição
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Mock para simular o DriverHandler
class MockDriverHandler:
    def average(self, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)  # Calcula a média de forma simples

def test_calculate_mean():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'value': 3.0, 'Success': True}}

def test_calculate_mean_with_negative_result():
    mock_request = MockRequest({"numbers": [-1, -2, -3]})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(HttpBadRequestError) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "A média calculada é negativa, o que pode indicar um erro nos dados."

def test_calculate_mean_with_invalid_data():
    mock_request = MockRequest({"numbers": ["a", 2, 3]})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Todos os números devem ser inteiros ou decimais."

def test_calculate_mean_without_numbers_field():
    mock_request = MockRequest({"values": [1, 2, 3]})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Body mal formatado! Certifique-se de incluir 'numbers'."
