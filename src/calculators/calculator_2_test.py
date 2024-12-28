from .calculator_2 import Calculator2
from typing import Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [1.2, 2.44, 3.11, 4.56, 5.99]})

    calc_2 = Calculator2()
    formated_response = calc_2.calculate(mock_request)
    print()
    print(formated_response)

    assert isinstance(formated_response, dict)  
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.07}}
