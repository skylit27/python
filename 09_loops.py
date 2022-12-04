## loops ##

# while

my_condition  = 0

while my_condition < 10:  #al while le podemos meter un else
    #my_condition +=1 si lo pongo aqui empieza en 1 pero si lo dejo como abajo empieza mostrando 1
    print(my_condition)
    my_condition +=1
else: print("Mi condicion es mayor o igual que 10") #es opcional

# si pusieramos un if  antes del else seria un if normal ya que no entraria como parte del while
print("la ejecucion continua")
    
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("mi condicion es 15")
        print("se detiene la ejecucion")
        break #detenemos la ejecion con brake y deja de ejecutar el while aunque sea menor que 20
        
#metemos un if dentro del while en este caso como va de 2 en 2 no pasa por el 15 y solo muestre el 20
    print(my_condition)

# For 

my_list = [35, 24, 62 , 52 , 30 ,30 , 17]

for element in my_list:
    print (element)

my_tuple = (35, 1.77, "Oce" , "Skylit", "Oce")

for element in my_tuple:
    print (element)

my_set = {"Oce", "Skylit", 24}

for element in my_set:
    print (element)

my_dict = {"Nombre" : "drackoss", "Apellido" : "skylit", "Edad" : 35, 1 : "python"}

for element in my_dict: #devuelve las claves
    print (element)
    if element == "Edad":
        break
    print("se ejecuta")
else:
    print ("El bucle for para mi diccionario ha finalizado") #cuando el bucle termiwna de iterar el diccionario imprime este mensaje

""" for element in list(my_dict.values()): #devuelve los values
    print (element) """


for element in my_dict: #devuelve las claves
    print (element)
    if element == "Edad": 
        continue #si usamos el continue aunque el "se ejecuta " esta despues del continue este se muestra a diferencia del break que rompe el ciclo donde este esta
    print("se ejecuta") #el continue hace que vuelva al for y por lo tanto muestra 1
else:
    print ("El bucle for para mi diccionario ha finalizado") #cuando el bucle termiwna de iterar el diccionario imprime este mensaje