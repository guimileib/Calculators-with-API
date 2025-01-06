# Bad request -> 400
class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'HTTP_UNPROCESSABLE_ENTITY'
        self.status_code = 422

try: 
    print('Estou no bloco try')
    raise HttpUnprocessableEntityError('Estou lançando uma exceção')
except Exception as exception:
    print('Estou no bloco except')
    print(exception.message)
    print(exception.name)
    print(exception.status_code)