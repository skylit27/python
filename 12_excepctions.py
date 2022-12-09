### exceptions handling ###
numberOne, numberTwo = 5 , 1


numberTwo = "1"

#el if else no nos salva de errores podriamos hacer una verificacion de tipo de dato pero no para manejar errores


"""
if numberOne > 3:
    print (numberOne + numberTwo)
else:
    print("No se cumplio")
"""

# print(numberOne + numberTwo)


#try except

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")

except:
    #se ejecuta si se produce una excepcion
    print("Se ha producido un error")


#try except else 

#el else y el finally son opcionales

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")

except:
    print("Se ha producido un error")

else: #se ejecuta si no se ha producido una excepcion
    print ("la ejecucion continua correctamente")

finally: #se ejecuta siempre
    print ("la ejecucion continua")


#excepciones por tipo 
try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")

except TypeError: #se ejecuta solo si se produce typeError
    print("Se ha producido un TypeError")

except ValueError: #se ejecuta solo si se produce typeError
    print("Se ha producido un ValueError")

#Captura de la inforamacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("no se ha producido un error")

except ValueError as error: #se ejecuta solo si se produce ValueError
    print(error)

except Exception as exception: #es una manera mas generica de capturar la informacion de la excepcion
        print(exception) 

