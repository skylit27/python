## Funciones ## 

#def es la palabra reservada para las funciones

def my_function ():
    print("esto es una funcion")


my_function()
my_function()
my_function()

def sum_two_values (first_value, second_value):
   print(first_value + second_value)


sum_two_values(5, 9)
sum_two_values(1213124, 45433)
sum_two_values("5", "7") #se esta concatenando
sum_two_values(1.4, 5.2)

#al ser un tipado debil no podemos poner un tipado especifico para la entrada de datos

#retornar parametros

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10,5) #guardamos el resultado de la funcion en una variable 
print (my_result)

my_result = sum_two_values(20,10)
print(my_result) #retorna none por que esta funcion no retorna nada ya que no tiene un return

def print_name(name, surname):
    print(f"{name} {surname}")

#mirar linea 36 y 37
print_name(surname = "skylit", name ="oce") # se ha reorneado el orden que tenia el print es decir estamos metiendolos en orden diferente

#default
def print_name_with_default (name,surname, alias= "Sin alias"):  # en alias asignamos un valor por defecto
    print(f"{name} {surname} {alias}")

print_name_with_default("oce", "skylit")
print_name_with_default("oce", "skylit", "sky")

def print_texts(*texts): #para imprimir un numero infinito de textos" "parametros dinamicos"
    for text in texts:
        print(text.upper()) #imprime los textos en mayusculas

print_texts("Hola","Python","Oce","Skylit") #numero de parametros dinamico
print_texts("Hola")
 