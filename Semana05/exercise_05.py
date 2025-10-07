'''
Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
'''

counter = 0
user_list = []
index = 0

while (counter < 10):
    user_number = int(input("Insert a number: "))
    user_list.append(user_number)
    counter += 1

for index_list in range(0,len(user_list)):
    if(user_list[index_list] > index):
        index = user_list[index_list]
    else:
        index = index
print(f"This is your List: {user_list}, The higher number is: {index}")
