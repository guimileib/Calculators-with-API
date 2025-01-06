from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import Request as FlaskRequest
from typing import Dict, List

class Calculator3:
    '''
     N numeros são colados como entrada
     Caso a variancia de todos esse numeros for menor que a multiplcação deles, é aprensetado 
     uma informação de sucesso ao usuario.
     Caso contrário, é apresentado uma informação de falha

     Obs: Para o calculo de variance, utilize o metodo "var" da biblioteca numpy
    '''
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
       body = request.get_json() # Pega o json do request
       input_data = self.__validate_body(body)

       variance = self.__calculate_variance(input_data)
       multiplcation = self.__calculate_multiplication(input_data)
       self.__verify_results(variance, multiplcation)

       formatted_response = self.__format_response(multiplcation)
       return formatted_response
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")

        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> List[float]:
        multiplication  = 1
        for num in numbers:
            multiplication *= num

        return multiplication
    
    def __verify_results(self, variance: float, multiplication: float) -> Dict:
        if variance < multiplication:
            raise Exception("Falha no processo: Variância menor que a multiplicação")
    
    def __format_response(self, variance: float) -> Dict:
        return { 
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True
            }
        }