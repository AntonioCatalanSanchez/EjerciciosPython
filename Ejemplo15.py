# -*- coding: utf-8 -*-

cadena="hola yo me llamo Antonio"

def devolvercaracteres(cadena):
    #lista=[cadena]
    print("los dos primeros caracteres: " + cadena[:2])
    print("los tres ultimos caracteres: " + cadena[-3:])
    print("cada dos caracteres: " + cadena[::3])
    print("sentido inverso: " + cadena[::-1])



devolvercaracteres(cadena)

