#01-Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

name = str("Migue")
lastname = str("Oviedo")
result_string = name + lastname
print(f"Result of String: {result_string}")
#Result of String: MigueOviedo

age = 39
#result_str_int = name + age
#print(f"Result String + Int: {result_str_int}")
print("""Result sum of string + int is:  
      Traceback (most recent call last):
        File "c:\Lyfter\Semana04\exercise_01.py", line 9, in <module>
            result_str_int = name + age
        TypeError: can only concatenate str (not 'int') to str""")

#result_int_str = age + name
#print(f"Result of int + string is: {result_int_str}")
print("""Result sum of int + string is: 
      Traceback (most recent call last):
        File "c:\Lyfter\Semana04\exercise_01.py", line 13, in <module>
            result_int_str = age + name
        TypeError: unsupported operand type(s) for +: 'int' and 'str'""")

list_one = [1,2,3,4]
list_two = [5,6,7,8]
result_list = list_one + list_two
print(f"Result sum list: {result_list}")
#Result sum list: [1, 2, 3, 4, 5, 6, 7, 8]

#result_str_list = name + list_one
#print(f"Result sum string + list: {result_str_list}")
print("""Result sum of string + list is:
        Traceback (most recent call last):
            File "c:\Lyfter\Semana04\exercise_01.py", line 30, in <module>
                result_str_list = name + list_one
                                  ~~~~~^~~~~~~~~~
                TypeError: can only concatenate str (not "list") to str""")

salary = 10.5
result_float_int = salary + age
print(f"Result sum float + int: {result_float_int}")
#Result sum float + int: 49.5

male = True
female = False
result_bool = male + female
print(f"Result sum boolean: {result_bool}")
#Result sum boolean: 1