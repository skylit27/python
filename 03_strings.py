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