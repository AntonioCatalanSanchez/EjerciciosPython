
def buscarValor(diccionario, clave):


    if(diccionario.get(clave)==None):
        raise ValueError("clave erronea")
    else:
        print diccionario.get(clave)








midiccionario={"Espania": "Madrid", "Italia": "Roma"}
clave=raw_input("introduce una clave: ")
buscarValor(midiccionario, clave)