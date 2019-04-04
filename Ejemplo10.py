

def generaPares(limite):
    numero=0


    while numero<limite:
        numero+=2
        yield numero



limite=int(input("introduzca el limite: "))

devolverpares=generaPares(limite)

print(next(devolverpares))
print(next(devolverpares))
print(next(devolverpares))
print(next(devolverpares))
print(next(devolverpares))