
def funcionDecoradoraPotencia(funcion_parametro):

    def funcionInterior(*args):

        print (pow(funcion_parametro(*args),11))
    return funcionInterior






@funcionDecoradoraPotencia
def operacion(a, b):

    resultado=a+b
    return resultado




operacion(2,3)