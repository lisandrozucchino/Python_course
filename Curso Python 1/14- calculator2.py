#una calculadora con más funciones
#pasos:
#1- recibir un número
#2- recibir una operación básica, validar que sea una de las 4 y luego proceder
#3- recibir un segundo número

def calculator():
    num1 = input("Por favor, ingrese un número: ")
    oper = input("Por favor, elija la operación a realizar (+, -, *, /): ")
    num2 = input("Ahora ingrese un segundo número: ")
    if oper == "+":
        print((float(num1) + float(num2)))
    elif oper == "-":
        print((float(num1) - float(num2)))
    elif oper == "*":
        print((float(num1) * float(num2)))
    elif oper == "/":
        print((float(num1) / float(num2)))
    else:
        print("No ingresaste una operación válida")

calculator()