# -*- coding: utf-8 -*-

lista = [1,2,3,4,5]

def sumalista(lista):
    x=0
    for i in lista:
       x=x+i

    print("la suma de la lista es " + str(x))


sumalista(lista)