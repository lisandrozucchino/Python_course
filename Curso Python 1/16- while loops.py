#Se indica que el código se ejecute hasta que se cumpla una condición.
#Todo el loop va a estar indentado dentro de "while".

#primero, una variable que sirva de condición:
i = 1

#después, indicar en el código que MIENTRAS algo se cumpla, hay que hacer X cosa.
#En este caso vamos a devolver el valor de la condición y, luego de hacerlo, aumentar en 1 el valor de dicha condición.
#De esa manera, el programa se acercará a cumplir la condición y, al hacerlo, saldrá del loop.
while i <= 10:
    print("i value is " + str(i))
    i = i + 1
print("And the loop is over because i= " + str(i))