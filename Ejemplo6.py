# -*- coding: utf-8 -*-


lista=[("Espania", "Madrid"), ("Francia", "Paris"), ("Portugal", "Lisboa"), ("Italia", "Roma")]


def devolverdiccionario(lista):

    midiccionario={}
    for i in range(len(lista)):
        #print lista[i]
        midiccionario[lista[i][0]]=lista[i][1]
        #midiccionario[España]="madrid"


    print midiccionario

devolverdiccionario(lista)