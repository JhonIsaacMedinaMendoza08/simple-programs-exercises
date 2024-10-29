#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6


ActualTime = int(input("Insert actual time, plese: "))
numberhours = int(input("Insert number of hours, plese: "))
futurehour = (ActualTime + numberhours) % 12

if futurehour == 0:
    futurehour = 12

print(f"""In {numberhours} hours, the clock will strike  {futurehour}
""")
