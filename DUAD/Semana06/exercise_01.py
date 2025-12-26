'''
Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame a la segunda.
'''

def function_two():
    print("Function Two")


def function_one():
    print("Function One")
    function_two()


function_one()
