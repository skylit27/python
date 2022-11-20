#Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)

print(my_int_to_str_variable)
print(type (my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables en un print
print(my_string_variable , my_int_variable, my_bool_variable)
print("Este es el valor de :", my_bool_variable)

#nontype
# print (type(print(my_string_variable , my_int_variable, my_bool_variable)))

#funciones del sistema

#len cuenta el largo de la cadena de texto

print(len(my_string_variable))

#variables en una sola linea

#tener CUIDADO por que se pueden cometer errores y no es una muy buena practica
name, surname, alias, edad = "Cesar", "Sanchez", "skylit", 24
print("Mi nombre es", name, "Mi apellido es", surname, "mi edad es", edad, "y mi alias es:", alias)

# input (puede servir con aplicaciones que trabajen con la terminal: scripts etc)

"""
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

"""

#haciendo pruebas con variables cambiando su valor (tipo)

name= 35
edad= "skylit"

print(name)
print(edad)


# ¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32

print(type(address))

#no se pudo es un tipado debil
