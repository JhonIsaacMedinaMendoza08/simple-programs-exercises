#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
 #de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
 #del triangulo, dado por el teorema de Pitágoras: c2=a2+b2

#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267


import math

cathetusA= int(input("Insert cathetus A , please: "))
cathetusB= int(input("Insert cathetus B , please: "))
hypotenuse = math.sqrt((cathetusA ** 2)+(cathetusB ** 2))

print(f"""The hypotenuse is: {hypotenuse}
""")
