## tuples ##

"""las tuplas son un conjunto de valores cerrados es decir son valores constanten no modificable a diferencia de las listas
que podemos modificar datos aqui son valores preinicializados"""

my_tuple = tuple() #estas son las 2 formas de definir una tupla
my_other_tuple = (35, 60, 40, 15)

my_tuple = (35, 1.74, "drackoss", "skylit","drackoss")

print(my_tuple)
print(type(my_other_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) error
#print(my_tuple[-6]) error

print(my_tuple.count("drackoss"))
print(my_tuple.index("skylit"))#nos dice cual es el indice del dato
print(my_tuple.index("drackoss")) #nos da el indice del primer dato que ha encontrado

# my_tuple[1] = 1.80 no se puede asignar por que las tuplas son constantes

print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))

my_tuple[4]= "oce"
my_tuple.insert(1,"oce skylit")
print(my_tuple)
print(type(my_tuple))

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))


