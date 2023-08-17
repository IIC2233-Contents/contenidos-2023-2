mi_variable = 10


def saludar():
    print("¡Hola!")


class MiClase:

    def __init__(self, argumento):
        self.argumento = argumento
        
    def __str__(self):
        return f"Hola, mi argumento es {self.argumento}." 
