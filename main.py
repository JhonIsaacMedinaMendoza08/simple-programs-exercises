#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3


score1 = float(input("Insert score contest 1: "))
score2 = float(input("Insert score contest 2: "))
scoreLab = float(input("Insert score contest LAB: "))


NC = (59.5 - (0.3 * scoreLab )) / 0.7
C3 = (((3 * NC ) - (score1 + score2)+ 1))
    

print(f"You need {round(C3)} on the final exam 3")