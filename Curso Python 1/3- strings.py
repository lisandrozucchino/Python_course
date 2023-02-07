#string
print("Fua, el Diego")

#el comando "\n" hace un salto de línea
print("Fua,\nel Diego")

#para agregar comillas al string se usa \"
print("Fua,\"el Diego\"")

#guardo la frase en una variable para hacer un print de la variable.
phrase = "Fua, el Diego"
print(phrase)

#parto la frase en tres partes para hacer un print de una concatenación
part_one = "Fua"
part_two = ", "
part_three = "el Diego"
print(part_one.upper() + part_two + part_three)

#busco conocer la longitud (length) de una de las variables.
print(len(part_one))

#si quiero puedo traer partes del string indicando la posición del caracter que deseo.
print(part_one[0] + part_one[1] + part_one[2])

#modificar una variable
new_part_one = part_one.upper()
print(new_part_one)

#buscar el index de un elemento del string
print(phrase.index("u"))#devuelve la ubicación de la primer "u" que encuentre (1).
print(phrase.index("Diego"))#devuelve la ubicación de la primer letra de la palabra(8).

old_goat = "Diego"
new_goat = "Lionel"

#reemplazo dentro de strings.
print(phrase.replace(old_goat, new_goat))#primero se indica el valor a reemplazar y luego el valor por el cual se lo reemplaza.
print(phrase.replace("Fua", new_part_one))