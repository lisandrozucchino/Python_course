#Una manera de organizar los datos en Python es en LISTAS (parecidos a los arrays de JS)

friends = ["Belu", "Mariano", "Alfredo", "Maxi", "Lio", "Pedro"]

#Quiero acceder a la lista u obtener datos de la misma.

#Cuántos elementos hay?
print(len(friends)) 

#Cuál es el primer elemento?
print(friends[0])
#CURIOSIDAD: se puede recorrer en sentido "antihorario" con números negativos.
print(friends[-2])
#Traer una porción de los datos
print(friends[0: 3]) #Incluye el primer dato que se pide, pero excluye el segundo que se indica. Si se deja en blanco el segundo, trae hasta el final de la lista
#Es posible modificar los elementos de las listas.
friends[3] = "TURBONATOR" #se modifica el elemento 3 (el cuarto de la lista)
print(friends)