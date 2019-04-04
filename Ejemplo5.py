import math
import random


picas=(1,2,3,4,5,6,7,8,9,10,'J','Q','K')
treboles=(1,2,3,4,5,6,7,8,9,10,'J','Q','K')
diamantes=(1,2,3,4,5,6,7,8,9,10,'J','Q','K')
corazones=(1,2,3,4,5,6,7,8,9,10,'J','Q','K')


barajaFrancesa=(picas,treboles,diamantes,corazones)


def devolverpoker(baraja):

    contador=0
    contador2=0
    poker="es poker"
    nopoker="no es poker"
    mano=[]

    #def funcion(x):
    # return x
    #mano1=map(valor,mano)

    for i in range(0,5):

        y=random.randrange(0,4)#saca carta de un palo aleatorio
        x = random.randrange(13)  # numero de la carta aleatorio
        #x=3 para ver si hay poker

        carta=baraja[y] [x]
        print carta
        mano.append(carta)

    x=set(mano)
    print x

    if len(x)<=2:

        print "es poker"
    else:
        print"no es poker"
"""
        for j in range(len(mano)):
            if carta==mano[j]:
                contador=contador+1

        if contador == 4:
            contador2=4


        contador=0
    if contador2==4:
        print(poker)
    else:
        print(nopoker)


"""
devolverpoker(barajaFrancesa)




