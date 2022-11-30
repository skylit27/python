#listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 53, 58, 30, 30]

pop_list = [11,24,35,50,11,22]

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

my_list.pop() # elimina el ultimo de la lista 
print(my_list) #aqui elimina el 30

print(my_list.pop()) # aqui nos devolvera 58 por que es el nuevo ultimo dato que elimino
 # el pop nos devuelve el ultimo dato que hemos eliminado por si lo necesitamos

print(my_list) #aqu verificamos que ya no tenemos el 58


#hacemos nuevamente un pop pero pasandole una posicion de lista
print(my_list.pop(0)) # en este caso es 35


print(my_list) #aqui solo queda 53 en la lista


"""es decir que si a pop no le pasamos ningun parametro de lista elimina el ultimo numero de la lista sin embargo tambien retorna el numero que
eliminamos, pero tambien podemos pasarle una posicion de lista y eliminara el dato de esa posicion y nos lo
retornara en caso de que lo necesitemos"""


#Guardamos el dato que eliminamos con pop en una variable

my_pop_element = pop_list.pop(2)
print(my_pop_element)
print(pop_list)

# si solo quieres eliminar un elemento sin tener el dato usamos del

del pop_list[2]
print(pop_list) #podemos ver que se elimino el 50

"""la diferencia entre el remove y el del es que con el remove eliminamos un dato que conocemos 
como vimos anterior mente eliminamos el 30 y este se elimino pero por que conocemos el dato
en el caso de del eliminamos un dato en una posicion de la lista, es decir del elimina por indice"""

pop_list.clear() #limpiamos la lista
print(pop_list)

my_list= "Hola Python" #convertimos la lista anterior a string # Es un tipado dinamico de python

print(my_list)
print(type(my_list))

my_list= ["Hola Python"] #aqui la volvemos a convertir en lista

print(my_list)
print(type(my_list))

#no se pueden crear constantes en python como tal, se puede definir en mayuscula para indicar que es una constante




