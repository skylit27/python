### sets ###

my_set = set()
my_other_set={}

print(type(my_set))
print(type(my_other_set)) #inicialmente es un dict

my_other_set = {"drackoss","skylit", 24}
print(type(my_other_set)) 

print(len(my_other_set))

my_other_set.add("oce skylit")
print(my_other_set) #un set no es una estructura ordenada

my_other_set.add("oce skylit") #un set no admite repetidos
print(my_other_set)

print("sky" in my_other_set) #nos permite realisar busquedas, retorna false por que no existe sky
print("skylit" in my_other_set) #aqui retorna true por que si existe skylit

my_other_set.remove("skylit") #hay operaciones que si podemos realizar como remove
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set)
my_set= {"skylit", "drackoss", 24}
my_list = list(my_set)
print(my_list)
print(my_list[0]) #hacer esto es muy arriesgado por que set no tiene un orden en los datos


my_other_set = {"java","python","Go"}

# my_new_set = my_other_set + my_set #asi no se pueden unir hay que usar union

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union(my_new_set)) #no aceptan repetidos por eso no se unen
print(my_new_set.union(my_new_set).union(my_set.union({"C#","JavaScript"})))