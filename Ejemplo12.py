
def insertarenLista(lista, elemento):

    for i in lista:

        if i == elemento:
            raise ValueError("el elemento ya existe en la lista")

    lista.append(elemento)


lista=["Antonio","Borja","Carlos"]


insertarenLista(lista, "Daniel")

print lista

