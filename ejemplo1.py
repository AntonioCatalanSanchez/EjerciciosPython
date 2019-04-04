def funcionmaximo(num1, num2, num3):
    if num1>num2 and num1>num3:
        print (num1)
    elif num2>num1 and num2>num3:
        print (num2)
    elif num3>num1 and num3>num2:
        print (num3)


numero1 = int(input("introduce el numero 1 "))
numero2 = int(input("introduce el numero 2 "))
numero3 = int(input("introduce el numero 3 "))

funcionmaximo(numero1,numero2, numero3)