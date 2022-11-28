#Strings

my_string = "Mi String"
my_other_string = "Mi Otro String"

print (len(my_string))
print (len(my_other_string))

print (my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"

print(my_new_line_string)


my_tab_string = "\tEs es un String con tabulacion"

print(my_tab_string)

my_scape_string = "\\tEs es un String \\n escapado"
print(my_scape_string)

#formateo

name, surname, age = "Drackoss", "Skylit", 24

print ("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #haciendolo con format
print ("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #haciendolo con %

print ("Mi nombre es " + name +" "+ surname + " y mi edad es " + str(age)) #asi es mas tedioso y es dificil hacer un buen codigo y se pudo el str por que age es un int y marca error

"""
nota: es mejor usar el porcentaje ya que le estamos asignando un formado en el caso de %d tenemos que pasarle un numero pero si intentamos pasarle un texto 
marca error en cambio con el primer ejemplo podemos pasarle cualquier tipo de dato y asi nos aseguramos de pasar un tipo dato que queremos
"""

print (f"Mi nombre es {name} {surname} y mi edad es {age}") #inferencia de datos #se pone la f antes


#Desempaquetado de caracteres

language = "python" #empieza del 0
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division

language_slice= language[1:3] #muestra los caracteres 1 y 3

print(language_slice)


language_slice= language[-2] #asi muestra el segundo caracter que esta antes del final

print(language_slice)


language_slice= language[:] #asi muestra todo

print(language_slice)

language_slice= language[0:6:2] 

print(language_slice)

#reverse

reversed_language= language[::-1] # el final empieza por -1

print(reversed_language)

#Funciones



print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
print("py" == "Py")
