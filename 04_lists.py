#listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 53, 58, 30, 30]

print(my_list)
print(len(my_list))

my_other_list = [35 , 1.74, "drackoss", "skylit"]

print(type(my_list))
print(type(my_other_list))
print(type(my_other_list[0]))


print(my_other_list[2])
print(my_other_list[-1])

#print(my_other_list[-5]) #error
#print(my_other_list[4]) #error

print(my_other_list.count("drackoss")) #count sirve para contar cuantas veces hay un dato
print(my_list.count(30)) #count sirve para contar cuantas veces hay un dato

age, height, name, surname = my_other_list #agarra el dato dependiendo de la posicion en la lista

print(name) #name es el tercer dato de my_other_list
print(age) 

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3], #cambiamos las posiciones
print(age) 

print(my_list + my_other_list) # suma de listas

my_other_list.append("skylit27") #con append agrego un nuevo dato a la lista, esta se va al final
print(my_other_list)

my_other_list.insert(1, "negro") 

print(my_other_list)

"""insert: inserta en una posicion de la lista 
un nuevo dato desplazando el dato que esta en 
esta posicion a la derecha en este caso el dato de la posicion 1 pasa
a la posicion 2
"""
my_other_list.remove("negro") #ponemos el dato a eliminar no la posicion en esta caso eliminamos negro #nota solo elimina 1 si hay 2 valores iguales o mas solo elimina el primer elemento
print(my_other_list)


my_list.remove(30) # aqui solo eliminara uno de los dos 30 que existen en la lista en este caso el primer 30 que encuentra
print(my_list)

my_list= "Hola Python" #convertimos la lista anterior a string # Es un tipado dinamico de python

print(my_list)
print(type(my_list))

my_list= ["Hola Python"] #aqui la volvemos a convertir en lista

print(my_list)
print(type(my_list))

#no se pueden crear constantes en python como tal, se puede definir en mayuscula para indicar que es una constante




