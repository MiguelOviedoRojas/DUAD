'''
#Para abrir un archivo y leerlo (El archivo queda abierto y robando memoria)

def open_and_print_file(path):
    arch = open(path)
    print(arch.read())

open_and_print_file("C:\Lyfter\Semana08\my_file.txt")

#Para Abrir un archivo y leerlo (Lo hacemos con with para abrir y luego cerrar el archivo para NO robar RAM)
def open_and_print_file(path):
    with open(path) as arch:
        print(arch.read())
    
    print("La variable 'file' ya no existe")
    print("El archivo ya no esta abierto")


open_and_print_file('C:\Lyfter\Semana08\my_file.txt')



#Para escribir dentro de un archivo
from datetime import datetime

def generate_time_log():
    current_time = datetime.now()
    return "Esto fue escrito a las " + current_time.strftime("%I:%M %p")

#Para escribir en un archivo SIN borrar la info existente (Usamos "a" en el with)
def write_time_log_to_file(file_path):
    log = generate_time_log()
    with open(file_path, "a") as arch:
        arch.write(log)


write_time_log_to_file("C:\Lyfter\Semana08\log_time.txt")


from datetime import datetime


def generate_time_log():
    current_time = datetime.now()
    return 'Esto fue escrito a las ' + current_time.strftime('%I:%M %p')

    
#Para escribir en un archivo SOBREESCRIBIMOS la info existente (Usamos "w" en el with)
def write_time_log_to_file(file_path):
    log = generate_time_log()
    with open(file_path, 'w') as arch:
        arch.write(log)

write_time_log_to_file('C:\Lyfter\Semana08\entries.log')
'''

#Para Escribir en un archivo (Sobreescribimos lo existente y le ponemos UTF-8 para que tome los signos en español)
def write_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as arch:
        arch.write(text)

Texto = """
Tradicionalmente, el número de especies de pingüinos a nivel mundial es de 17.
En 2006, se cambió este número a 18, cuando se empezó a reconocer al
pingüino saltarrocas como dos especies distintas:
el pingüino saltarrocas austral y el pingüino saltarrocas norteño.
"""

write_text_to_file("C:\Lyfter\Semana08\log_time.txt",Texto)