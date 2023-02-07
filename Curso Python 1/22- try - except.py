#try se utiliza para que un error (por ejemplo, esperar que el usuario ingrese un número pero termine ingresando un string) no detenga la ejecución del programa. Except es lo que devuelve en caso de detectar un error.

try:
    number = int(input("Please, write a number: "))
    print(number)
except:
    print("That's not a valid number, you bitch")

#hay distintas opciones para el "except", a los fines de no tener una sola respuesta para todos los errores que puedan aparecer.

try:
    #value = 10/0    
    number: int(input("Please, now write a real number: "))
    print(number)
except ZeroDivisionError:
    print("You tried to divide by zero, that's impossible.")
except ValueError:
    print("You entered a wrong value")