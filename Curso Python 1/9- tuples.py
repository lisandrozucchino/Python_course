#los tuples se parecen a las listas en el hecho de contener diferentes elementos.
#los tuples son inmutables. No pueden ser modificados.
#para crear un tuple, se hace de la siguiente manera: "new_name = ()" y dentro del paréntesis se indican los elementos.

#coordinates será un tuple.
coordinates = (4, 5)

#para acceder a los datos de un tuple, puedo utilizar los mismos métodos que se usan con una lista, pero no los de modificación.
print(coordinates[0])
print(coordinates)

#EXPERIMENTO: creo voy a crear otro tuple y una lista, para intentar combinarlos entre si.
experimento = ("Zacha", "Noe")
planetas = ["Marte", "Urano", experimento[0]]
print(experimento)
print(planetas)

#al final de "planetas" se agregan los elementos de "experimento"
planetas.extend(experimento)
print(planetas)

#elimino el último elemento de "planetas", que originalmente estaba en el tuple pero, al momento de entrar en la lista, se vuelve susceptible a los métodos de las listas.
planetas.pop()
print(planetas)


#es posible crear una LISTA de tuples. Entonces los elementos que se inserten serán inmutables PERO susceptibles a todos los métodos de las listas, entonces pueden ser reemplazados, eliminados, agregados, etc etc etc.
set_of_coordinates = [(4, 2), (3, 6), ("Mario", "Marcelo", "Eduardo")]
print(set_of_coordinates)
print(set_of_coordinates[2])
set_of_coordinates.append((90, 140))
print(set_of_coordinates)
set_of_coordinates.pop()
print(set_of_coordinates)
set_of_coordinates[1] = ("OH YES")
print(set_of_coordinates)
