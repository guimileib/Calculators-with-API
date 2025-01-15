from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import Request as FlaskRequest
from typing import Dict, List
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    '''
    Seguindo exemplo dado pelo instrutor nesse módulo, 
    adicione uma nova rota que retorne a média entre uma 
    lista de números fornecida em uma requisição POST. 
    '''
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        mean = self.__calculate_mean(input_data)
        self.__verify_results(mean)

        formatted_response = self.__format_response(mean)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado! Certifique-se de incluir 'numbers'.")

        input_data = body["numbers"]
        if not all(isinstance(num, (int, float)) for num in input_data):
            raise HttpUnprocessableEntityError("Todos os números devem ser inteiros ou decimais.")

        return input_data

    def __calculate_mean(self, numbers: List[float]) -> float:
        return self.__driver_handler.average(numbers)

    def __verify_results(self, mean: float) -> None:
        if mean < 0:
            raise HttpBadRequestError("A média calculada é negativa, o que pode indicar um erro nos dados.")

    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": mean,
                "Success": True
            }
        }
