cadena1="hola me llamo antonio"
cadena2="hola me llamo manuel"


print cadena1.find(cadena2)

def devolvercadenas(cadena1,cadena2):

    if(cadena1.find(cadena2)):
        print cadena2


def alfabeticamente(cadena1,cadena2):
    
    if(cadena1<cadena2):
        print cadena1
    else:
        print cadena2




devolvercadenas(cadena1,cadena2)
alfabeticamente(cadena1,cadena2)