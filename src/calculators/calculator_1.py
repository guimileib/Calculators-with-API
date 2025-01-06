from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
class Calculator1:
    '''
    Um número é recebido e dividido por 3. 
    A primeira parte é dividida por 4 e somada com 7. Após isso é elevada ao quadrado e somada com 0.257.
    A segunda parte é elevada a 2.121 e dividida por 5 e somada com 1.
    A terceira parte se mantem no mesmo valor
    Por fim é somado esses 3 valores e entregado o resultado. -> 
    '''
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json # pega a informação que o usuário manda na requisição
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        calc_result = first_process_result + second_process_result + splited_number
        response = self.__format_response(calc_result)

        return response
    
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257 # o certo é multiplicada ou somada??
        return second_part
    
    def __second_process(self, second_number: float)-> float:
        first_part = (second_number ** 2.121)
        second_part = (first_part / 5) + 1
        return second_part
    
    def __format_response(self, calc_result: float) -> Dict:
        return { # Formata a forma que o valor vai aparecer para o usuário
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }