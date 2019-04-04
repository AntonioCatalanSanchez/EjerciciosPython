numero1=int(input("introduce el primer numero: "))
numero2=int(input("introduce el segundo numero: "))


def maximodivisor(num1,num2):
    resto = 0
    while num2>0:
        resto = num2
        num2=num1%num2
        a = resto
    return a


print("el maximo comun divisor de " + str(numero1) + " y " + str(numero2) + " es " , maximodivisor(numero1,numero2))