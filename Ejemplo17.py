def devolverlineas(archivo, n):
    miarchivo = open(archivo, "r")
    lineas = miarchivo.read()

    linea = lineas.splitlines()

    x=0
    while x<n:
        print(linea[x])
        x=x+1


archivo="C:\Users\cxb0271\Documents\mitexto.txt"

numlineas = int(input("cuantas lineas quieres que aparezcan: "))
devolverlineas(archivo, numlineas)