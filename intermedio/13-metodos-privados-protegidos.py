class BaseClass:
    def __init__(self):
        self._protected_variable = 'Esto es una variable protegida'
        self.__private_variable = 'Private'

    def _protected_method(self):
        print('Este es un metodo protegido')

    def __private_method(self):
        print('Esto es un metodo privado')

    def public_method(self):
        self.__private_method()

base = BaseClass()
print(base._protected_variable)
base._protected_method()

base.public_method()

base.__private_method()
    #Error: no encuentra el método privado
print(base.__private_variable) 
    #Error: no encuentra la variable privada