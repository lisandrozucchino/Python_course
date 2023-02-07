#los loops "for" recorren un elemento (lista, string, tuple..) y hacen algo por cada uno.
#el nombre de la variable puede ser cualquiera, siempre y cuando se respete dentro del loop.
for letter in "Elvis":
    print(letter)

friends = ["Belu", "Mariano", "Alfredo", "Maxi", "Lio", "Pedro"]
for friend in friends:
    #por cada elemento en la lista, hará algo. Incluso puede hacer lo mismo X veces, siendo X la cantidad de elementos en la lista.
    print(friends[1])

#puedo indicar un rango de números que indicará la cantidad de veces que lo hará.
for num in range(10):
    print(num)

#Puedo hacerlo a partir de una variable e indicar un número inicial para el rango. Range no incluirá el último elemento, así que se puede suplir con un +1.
my_range = int(input("Pick a number between 3 and 8"))

for unit in range(2, my_range):
    print(unit)
