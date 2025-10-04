#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Enter your name: ").upper()
lastname = input("Enter your lastname: ").upper()
age = int(input("Enter your age: "))

if(age <= 0):
        print("""
        Incorrect Age.
        Age must be greater than 0
        """)
elif(age < 3):
    print(f"{name} {lastname} is a Baby")
elif(age < 11):
    print(f"{name} {lastname} is a Child")
elif(age < 13):
    print(f"{name} {lastname} is a Pre-Teen")
elif(age < 18):
    print(f"{name} {lastname} is a Teenager")
elif(age < 26):
    print(f"{name} {lastname} is a Young Adult")
elif(age < 60):
    print(f"{name} {lastname} is a Adult")
else:
    print(f"{name} {lastname} is a Older Adult")
