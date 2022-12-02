## dicts ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "drackoss", "Apellido" : "skylit", "edad" : 35, 1 : "python"}

my_dict = {
    "Nombre" : "Drackoss",
    "Apellido" : "Skylit",
    "edad" : 35,
    "Lenguages": {"Python", "JavaScript", "Go"}, 
    1 : 1.77
    
    }

print(my_dict)
print(my_other_dict)


print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Lenguages"]) #imprimimos el dato correspondiente con la clave que ingresamos

my_dict["Nombre"] = "Oce Skylit" #asignamos un nuevo valor a la clave nombre
print(my_dict["Nombre"])

print(my_dict[1])#la clave es un numero entero entonces lo pasamos como entero y no como un string

my_dict["pais"] = "Mexico" #agregamos una nueva clave y dato al diccionario
print(my_dict)

del my_dict["pais"] # a diferencia de las listas, tuplas aqui no hay remove podemos borrar una Clave/Dato con del y poniendo la clave
print(my_dict)

print("Skylit" in my_dict) # en este caso estamos buscando el dato y nos dara false aunque si este el dato pero tenemos que buscar por clave
print("Apellido" in my_dict) #aqui nos da true por que buscamos por la clave

print(my_dict.items()) # nos retorna un listado de items
print(my_dict.keys()) # nos retorna solo las claves
print(my_dict.values()) # nos retorna los datos

my_new_dict = my_other_dict.fromkeys(("Nombre",1)) #nos sirve para crear un diccionario sin datos
print(my_new_dict)