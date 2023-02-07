#Vamos a hacer una función que reciba tres parámetros numéricos y devuelva el mayor.

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(str(num1) + " es el mayor")
    elif num2 > num1 and num2 > num3:
        print(str(num2) + " es el mayor")
    elif num3 > num1 and num3 > num2:
        print(str(num3) + " es el mayor")
    else:
        print("Hay algún número igual a otro")

max_num(4, 2, 1)
max_num(1, 6, 2)
max_num(2, -3, -8)
max_num(2, 2, 1)

#Puedo, claro está, guardar los números dentro de variables para usarlos luego.
a = input("Por favor, ingrese un número: ")
b = input("Por favor, ingrese un número: ")
c = input("Por favor, ingrese un número: ")

max_num(a, b, c)