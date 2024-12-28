import numpy 
from typing import List

class NumpyHandler: # Classe para manipulação de dados com a biblioteca numpy
    def __init__(self) -> None: # Inicializa a classe
        self.__np = numpy # Importa a biblioteca numpy

    def standard_derivation(self, numbers: List[float]) -> float: # Função para calcular o desvio padrão
        std_dev = self.__np.std(numbers) # Desvio padrão
        return float(std_dev)