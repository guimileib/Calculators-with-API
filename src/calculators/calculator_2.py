from flask import request as FlaskRequest
from typing import Dict, List
from drivers.numpy_handler import NumpyHandler

class Calculator2:
    '''
    N números são enviados
    Todos eses N números são multiplicados por 11 e elevados a potencia de 0.95
    Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor
    (1/result)
    Dica: Utilize a bibloteca Numpyy para calcular o desvio padrão
    '''
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        formated_response = self.__format_response(calculated_number)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")

        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        numpy_handler = NumpyHandler()
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = numpy_handler.standard_derivation(first_process_result)
        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return { # Formata a forma que o valor vai aparecer para o usuário
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }
    
    
