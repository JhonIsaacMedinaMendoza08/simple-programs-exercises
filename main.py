M = 67  # Mass in grams for a large egg
rho = 1.038  # density g/cm^3
c = 3.7  # Heat capacity in J/(g K)
K = 5.4e-3  # Thermal conductivity in W/(cm·K)
Tw = 100  # Boiling point of water in °C
Ty = 70  # Maximum yolk temperature in °C


def time_to_boil(To):
    numerator = (M**(2/3)) * c * (rho**(1/3)) * K * (3.141592653589793**2) * ((4 * 3.141592653589793 / 3)**(2/3))
    
    # log(a) - log(b) = log(a/b)
    term1 = 0.76 * To - Tw
    term2 = Ty - Tw
    log_term = term1 / term2

    # Calculamos el tiempo
    t = numerator * log_term
    return t

original_temperature = float(input("Enter the original temperature of the egg (°C): "))
time = time_to_boil(original_temperature)

print(f"The time required to reach the maximum temperature is:{time:.2f} seg")

