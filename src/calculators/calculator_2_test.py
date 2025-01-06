from src.calculators.calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Mock do driver para testar a integração 
class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]) -> float:
        return 3.14
        

# Teste de integração entre o Calculator2 e o NumpyHandler
def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [1.2, 2.44, 3.11, 4.56, 5.99]})

    driver = NumpyHandler()
    calc_2 = Calculator2(driver)
    formated_response = calc_2.calculate(mock_request)

    assert isinstance(formated_response, dict)  
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.07}}

# 
def test_calculate():
    mock_request = MockRequest(body={"numbers": [1.2, 2.44, 3.11, 4.56, 5.99]})

    driver = MockDriverHandler()
    calc_2 = Calculator2(driver)
    formated_response = calc_2.calculate(mock_request)

    assert isinstance(formated_response, dict)  
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.32}}