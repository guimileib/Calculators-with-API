import numpy 
from typing import List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface): # Classe para manipular o numpy e calcular o desvio padrão 
    def __init__(self) -> None: # Inicializa a classe
        self.__np = numpy # Importa a biblioteca numpy

    def standard_derivation(self, numbers: List[float]) -> float: # Função para calcular o desvio padrão
        std_dev = self.__np.std(numbers) # Desvio padrão
        return float(std_dev)
    
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers) # Variância
        