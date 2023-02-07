#Un diccionario es una estructura de datos que permite guardar datos en "pares": "keys" and "values".
#una key equivaldría a la palabra, y el value a la definición de la misma.

#este ejemplo guarda la forma abreviada (keys) y los nombres completos (values) de los meses del año.
#las Keys deben ser únicas. Pueden ser números también. Tienen que cumplir la condición de ser únicas.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

#Cómo acceder al diccionario:
print(monthConversions["Feb"])

#get permite tener un valor "default" en caso de buscar una key que no exista en el diccionario.
print(monthConversions.get("Gro", "That's not a month"))
