### classes ###
#los nombres de las clases se escriben con camelCase (la primera letra de cada palabra mayuscula)

class MyEmptyPerson:
    pass # sirve para intentar que se ejecute en este caso si quitamos el pass la clase marcara error

print(MyEmptyPerson)#se puede llamar una clase con parentesis o sin
print(MyEmptyPerson())


class Person: #en la linea sig se define el constructor
    def __init__(self, name, surname): #el init es un constructor de clase
        self.name = name #self se refiere a el mismo
        self.surname = surname





my_person = Person("oce","skylit") #puede recivir los valores name y surname
print(my_person.name)#son las propiedades que creamos con self
print(my_person.surname)
print(f"{my_person.name} {my_person.surname}")


class Person2: #en la linea sig se define el constructor
    def __init__(self, name, surname, alias = "sin alias"): #el init es un constructor de clase
        self.full_name = f"{name} {surname} {alias}" #self se refiere a el mismo #propiedad publica
        self.__name = name  #propiedad privada a la cual no se puede acceder y no podemos modificar
    
    def get_name(self): #hacemos una lectura y retornamos el valor __name ya que no podemos a acceder  a el
        return self.__name
        
    

    
    def walk(self): #usamos self para llamar a la misma clase y en este caso poder acceder a full name
        print(f"{self.full_name} esta caminando") 

my_person = Person2("oce", "skylit")
print(my_person.full_name)
# print(my_person.__name) # no podemos acceder al valor por que es privado---- ver linea siguien
print(my_person.get_name())
my_person.walk()


my_other_person = Person2("Oce", "skylit","oceskylit")
print(my_other_person.full_name)
my_other_person.full_name = "Oce Skylit OceSky27" #se puede acceder a una propiedad de la clase y modificarla sin necesidad de llamar al constructor
print(my_other_person.full_name) 

my_other_person.full_name = 666
print(my_other_person.full_name)