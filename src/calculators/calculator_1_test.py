from .calculator_1 import Calculator1
from pytest import raises
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"number": 1 })
    calc = Calculator1()   

    response = calc.calculate(mock_request) # request é pego do json
    print()
    print(response)
    # Formato da resposta - Caso os nomes mudem, o teste falha
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da respostas
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1 })
    calc = Calculator1()

    with raises(Exception) as excinfo:
        calc.calculate(mock_request)

    assert str(excinfo.value) == "body mal formata"