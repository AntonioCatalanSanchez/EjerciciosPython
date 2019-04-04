# -*- coding: utf-8 -*-

def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False


# lista que contendra los valores multiples

def multiplenumero(numero):

        # bucle del 1 al 100
        for i in range(numero):

            if multiple(i, 3):
                yield i



generador=multiplenumero(20)

print (next(generador))
print (next(generador))
print (next(generador))
print (next(generador))
print (next(generador))
print (next(generador))
print (next(generador))
