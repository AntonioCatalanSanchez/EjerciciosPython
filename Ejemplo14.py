class Fraccion():

    def __init__(self, x, y):
        self.dividendo=x
        self.divisor=y

    def __str__(self):

        self.division = str(self.dividendo/self.divisor)
        cadena=str(self.dividendo)+ "/" + str(self.divisor)
        return cadena


    def factorcomundivisor(self, nuevaFraccion):

        resto=0
        a=self.divisor
        b=nuevaFraccion.divisor

        if a > b:
            mayor = a
        else:
            mayor = b

        while (True):
            if ((mayor % a == 0) and (mayor % b == 0)):
                lcm = mayor
                break
            mayor += 1

        c=mayor

        dividendo1=self.dividendo*nuevaFraccion.divisor
        dividendo2=nuevaFraccion.dividendo*self.divisor
        sumadividendo=dividendo1+dividendo2
        fraccion3=Fraccion(sumadividendo,c)
        return fraccion3


    def multiplicar(self, nuevaFraccion):

        nuevodividendo=self.dividendo*nuevaFraccion.dividendo
        nuevodivisor=self.divisor*nuevaFraccion.divisor

        fraccion3=Fraccion(nuevodividendo,nuevodivisor)
        fraccion3.simplificar()
        return fraccion3


    def simplificar(self):

        a = self.dividendo
        b = self.divisor

        while b != 0:
            a, b = b, a % b
        c= a
        self.divisor=self.divisor//c
        self.dividendo=self.dividendo//c
        return self

miFraccion=Fraccion(20,5)
miFraccion2=Fraccion(40,8)

print("primera fraccion:  "+str(miFraccion))
print("primera fraccion simplificada  " + str(miFraccion.simplificar()))
print("segunda fraccion:  "+str(miFraccion2))
print("segunda fraccion simplificada  " + str(miFraccion2.simplificar()))

print("suma:  ")+ str(miFraccion.factorcomundivisor(miFraccion2))
print("multiplicacion:  ")+str(miFraccion.multiplicar(miFraccion2))



