
print "---------EJERCICIO AREA TRIANGULO--------------"

areaTriangulo=lambda base,altura:(base*altura)/2

print "el area del triangulo es ",areaTriangulo(5.0,7.0)


print "---------EJERCICIO MAP LISTA POR CINCO--------------"

listaNumeros=[2,6,8,4,5,6,7]

def numporcinco(numero):
    numero=numero*5
    return numero



listaNumerosporCinco=map(numporcinco, listaNumeros)#map para multiplicar toda la lista por cinco a traves de la funcion anterior

print "lista: ", listaNumeros

print "Lista multiplicada por cinco: ", listaNumerosporCinco




print "---------EJERCICIO CON FILTER--------------"


lista=[8,5,9,6]

print "lista de numeros: ", lista
print"lista multiplos de 3: ",list(filter(lambda x: x%3==0, lista))




