import math

Temp_inicial = int(input("Enter the initial temperature of the egg: "))
MG = 67  # Mass in grams for a large egg
MP = 47  # Mass in grams for a small egg
P = 1.038  # density g/cm^3
c = 3.7  # Heat capacity in J/(g K)
K = 5.4 * math.pow(10, -3)  # Thermal conductivity in W/(cm·K)
Tw = 100  # Boiling point of water in °C
Ty = 70  # Maximum yolk temperature in °Cç


Numerator = math.pow(MG, (2/3)) * (c * math.pow(P, (1/3)))
Denominator = (K * math.pow (math.pi, 2))  * math.pow((4*math.pi) / 3,(2/3))
R1 = Numerator/Denominator

r2 = math.log(0.76*((Temp_inicial - Tw)/(Ty - Tw)))

TimeSeg = R1 * r2
TimeMin = round(TimeSeg/60)

print (f"""The maximum time to prepare it in the cup is {TimeSeg} seg    """)
print (f"""The maximum time to prepare it in the cup is {TimeMin} min    """)
