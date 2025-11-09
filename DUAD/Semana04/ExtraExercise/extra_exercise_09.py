#3. **Convertidor de unidades de temperatura**
    #- Pida al usuario ingresar una temperatura en Celsius
    #- Conviértala a Fahrenheit y Kelvin
    #- Muestre los tres valores


celsius_temp = float(input("Insert Celsius Temperature: "))
fahrenheit_temp = float(celsius_temp * 9/5) +32
kelvin_temp = float(celsius_temp + 273.15)

print(f"Fahrenheit Temperature is: {fahrenheit_temp}")
print(f"Kelvin Temperature is: {kelvin_temp}")