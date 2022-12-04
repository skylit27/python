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