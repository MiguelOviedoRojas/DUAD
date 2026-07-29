#2. Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.
    #1. *Ejemplos*:
        #1. 73 → 20.27
        #2. 50 → 13.88
        #3. 120 → 33.33

speed_mts = 0

speed_km = int(input("Insert speed in KM: "))

speed_mts = (speed_km * 1000) / (60 * 60)

print(f"The speed meters/second is: {speed_mts}")