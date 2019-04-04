# -*- coding: utf-8 -*-
"""
def cifrarlineas(fichero1):
    fichero = open(fichero1, "r")
    lineas = fichero.read()
    linea = lineas.splitlines()
    clave=13

    """
mensaje="hola mundo"

def obtenerMensajeTraducido(fichero1, fichero2):
    clave=13
    fichero = open(fichero1, "r")
    lineas = fichero.read()
    linea = lineas.splitlines()
    traduccion = ''

    for simbolo in lineas:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave
            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduccion += chr(num)
        else:
            traduccion += simbolo
    f=open(fichero2, "w")
    f.write(traduccion)
    return traduccion



fichero1="C:\Users\cxb0271\Documents\mitexto.txt"
fichero2="C:\Users\cxb0271\Documents\mitextoencriptado.txt"


print(obtenerMensajeTraducido(fichero1, fichero2))

#cifrarlineas(fichero1)