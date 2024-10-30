#Parte decimal
#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19

def decimal(number):
    if number < 0:
        return abs(number) - int(abs(number))
    return number - int(number)

number2 = float(input("please, enter the number: "))
decimal2 =  decimal(number2)

print(decimal2)

