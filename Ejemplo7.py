import collections
cadenatexto=raw_input("introduce una cadena de texto: ")
#cadenatexto="hola hola hola me me llamo antonio"

def palabrasRepetidas(cadenatexto):

    midiccionario={}
    palabras = cadenatexto.split()


    for i in range(len(palabras)):

        x = palabras[i]
        contador = palabras.count(x)
        midiccionario[palabras[i]]=contador

    print midiccionario







palabrasRepetidas(cadenatexto)