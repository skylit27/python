### modules ###

import my_module # importamos el archivo modulo
# from 10_functions import sum_two_values ------------ #el tipo de nomenclatura no es valido para los modulos, ya que empíeza con numeros

my_module.sumValue(5,6,1)
my_module.printValue("hola python")


from my_module import sumValue, printValue#si lo hacemos asi podemos hacer operaciones directas ver linea 11 u 12
sumValue(5, 6 , 1)
printValue("hola sky")

import math

print(math.pi) 

print(math.pow(2, 8)) #potencia 2 a la 8

from math import pi as pi_value # le asignamos un alias con as

print(pi_value)