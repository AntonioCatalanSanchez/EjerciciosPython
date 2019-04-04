


def funcionDecoradora(funcion_parametro):

    def funcionInterior(*args):
        while True:
            if x%2==0:
                funcion_parametro(*args)
                yield x

    return funcionInterior





@funcionDecoradora
def pares(x):
       x=x+2
       return x



x=4

pares(x)

generador=pares(x)

print(next(generador))
print(next(generador))
print(next(generador))


generador=pares(x)

#print(generador)



