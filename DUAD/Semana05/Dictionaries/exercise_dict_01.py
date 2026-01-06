'''
Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`
'''


dict_hotel = {
    "name": "pacifico",
    "number_of_stars": 3,
    "rooms": [
        {
            "room_number":1,
            "floor":1,
            "price":100
        }
    ],
}


print(dict_hotel["name"])
print(dict_hotel["rooms"][0])

