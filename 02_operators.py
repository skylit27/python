#operadores Aritmeticos

print (3 + 4)

print (3 - 4)

print (3 * 4)

print (3 / 4)

print (10 % 3 )

print (10 // 3 )

print (2 ** 3 )
print (2 ** 3 + 3 -7 / 1 // 4)

print ("Hola " +"python" )

print ("Hola " + str(5) ) # el 5 se convierte en string 

print ("Hola " * 5 ) # se multiplica


print ("Hola " * (2 ** 3 ) )

my_float = 2.5 * 2 # al ser un floar no se puede multiplicar abajo, hay que pasarlo a entero

print ("hola " * int(my_float))



#operadores comparativos

print ("Aqui empieza operadores comparativos")

print (3 > 4)
print (3 < 4)
print (3 >= 4)
print (3 <= 4)
print (3 == 4)
print (3 != 4)

print ("Hola" > "python" )
print ("Hola" < "python")
print ("aaaa" >= "abaa") #ordenacion alfabetica por ASCII(teniendo en cuenta las mayusculas (si afectan pero solo es ejemplo))
print (len("aaaa") >= len("abaa")) #Cuenta caracteres
print ("Hola" <= "python")
print ("Hola" == "Hola")
print ("Hola" != "python")

#operadores Logicos

print ("operadores Logicos")  #nota practicarlas de manera individual

print ( 3 > 4 and "Hola" > "python") # && #dan false y false
print ( 3 > 4 or "Hola" > "python") # || #dan false y false

print ( 3 < 4 and "Hola" < "python") #true y true da true
print ( 3 < 4 or "Hola"> "python")  #true y false da true

print (3 < 4 or ("Hola" > "python" and 4 == 4))


print (not (3 > 4 )) # != # da falso pero con el not lo cambia al verdadero