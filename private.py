class MyClass:
    
    # metodo publico
    def registry(self) -> None:
        print('Start process')
        self.__verify()
        self.__verify_registry()
        self.__insert_data()

    # metodo privado 
    #conteudo dentro dessa classe so é acessivel por outra classe    
    def __verify(self) -> None:
        print('verify data 2')
    
    def __verify_registry(self) -> None:
        print('verify registry')

    def __insert_data(self) -> None:
        print('insert in DB')

    # Métodos especiais [__], uso de dois underlines antes

obj = MyClass()
obj.registry()