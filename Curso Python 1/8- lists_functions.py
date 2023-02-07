#Funciones para trabajar con listas
lucky_numbers = [3, 5 , 1 , 26, 31, 44, 27]
friends = ["Pedro", "Maxi", "Mariano", "Belu", "Alfredo", "Zacha", False, False, True, True]
print(friends)

#append agrega un elemento al final de la lista
friends.append("Cascote")
print(friends)

#insert agrega un elemento en el lugar de la lista que le indique.
friends.insert(1, "Steven")
print(friends)

#remove quita el elemento que se desee.
friends.remove("Zacha")
print(friends)

#clear borra todos los elementos.
friends.clear()
print(friends)

friends = ["Pedro", "Maxi", "Mariano", "Belu", "Alfredo", "Zacha"]
print(friends)

#pop elimina el último elemento de la lista.
friends.pop()
print(friends)

#index busca el elemento que quiero encontrar e indica su ubicación PERO DA UN ERROR SI NO ENCUENTRA EL ELEMENTO.
print(friends.index("Belu"))

#count cuenta los elementos similares.
friends.append("Cascote")
friends.append("Cascote")
friends.append("Cascote")
print(friends.count("Cascote"))

#sort ordena los elementos en forma ascendente (si son números) o alfabéticamente (si son strings). Da error en caso de tener más de un tipo de dato en la lista
lucky_numbers.sort()
friends.sort()
print(lucky_numbers)
print(friends)

#reverse invierte el orden de la lista, no necesariamente lo hace ahora "de mayor a menor", sino que toma el último elemento y lo coloca primero y así
#sucesivamente.
friends = ["Pedro", "Maxi", "Mariano", "Belu", "Alfredo", "Zacha"]
print(friends)
friends.reverse()
print(friends)

#puedo copiar una lista, crear una nueva variable que contenga una copia de la lista de otra.
new_friends = friends.copy()
print(new_friends)

#extend agrega los elementos de una lista a otra.
friends.extend(lucky_numbers)
print(friends)

x = {1,2,3,4,5}
x.add(5)
print(x)
