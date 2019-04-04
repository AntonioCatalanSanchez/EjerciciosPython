


def funcionvocales(caracter):
    if caracter=="a" or  caracter=="e" or caracter=="i" or caracter=="o" or caracter=="u":
        print("el caracter introducido es una vocal")
    else:
        print("el caracter introducido es una consonante")

vocal=raw_input("introduce el caracter ")

opcion = vocal.lower()

funcionvocales(opcion)