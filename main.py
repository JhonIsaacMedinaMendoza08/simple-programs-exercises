#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75

FirstNote = int(input("Enter your first note: "))
SecondNote = int(input("Enter your Second note: "))
thirdNote = int(input("Enter your third note: "))
FourthNote = int(input("Enter your fourth note: "))

print (F"""The average is : {(FirstNote+SecondNote+thirdNote+FourthNote)/4}""")