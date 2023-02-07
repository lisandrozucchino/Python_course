#Para hacer una suma a partir de los números que ingrese el usuario necesito dos campos de "input" y uno de "print" con el resultado
#El problema acá es que todo lo que ingresa el usuario es, en primera instancia, un string.
from math import *

print("Welcome to my first calculator. Let's add some numbers")
number_1 = input("Please, write a number: ")
number_2 = input("And now, write a second number: ")
#Por el momento, los dos números son strings por lo cual una "suma" sería una concatenación.
#variante 1
#agrego "int" delante de las variables para convertirlas en números enteros. Pero esto fallaría si hay decimales.
#Lo que se utiliza en caso de poder existir decimales es "Float"
resultado = (float(number_1) + float(number_2))
print("After storing the result in a different variable, I can tell you that your result is: " + str(round(resultado)))#agrego ROUND para que redondee

#variante 2
print("Also, I can make the addition here, in this print, and tell you that the result is: " + str(float(number_1) + float(number_2)))