 ### Conditionals ###


 #mientras tenemos tabulacion el codigo seguira siendo parte de la condicion

my_condition = True #si es verdadero se imprime pero si es falsa no se ejecuta


if my_condition : # es lo mismo que if my_condition == True:
    print("se ejecuta la condicion del if")

    my_condition = 5 * 2

if my_condition == 10 : 
    print("se ejecuta la segunda condicion")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")

elif my_condition == 1: #este es un else if
    print("Es igual a 1")

else: 
    print("es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecucion continua")


my_list = [1, 2 ,3 ,4]


if len(my_list) == 4:
        print("tiene 4 valores")


my_string = ""

if not my_string: # estamos negando que mi cadena de texto no este vacia
    print ("my cadena de texto es vacia")

if my_string == "Mi cadena de textoo":
    print ("Estas cadenas de texto no coinciden")