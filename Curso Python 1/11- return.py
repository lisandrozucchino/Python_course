#Return es obvio, es lo que una función devuelve luego de ser invocada.
#return indica el final de la función. Una vez que devuelve un valor, Python sale de la función.

def tripler(a):
    resultado = int(a) * 3
    return resultado

#si sólo invoco la función con el dato que quiero, no pasa nada en la pantalla porque no hay un print. La función devuelve el resultado, pero
#no hago nada con él.
tripler(3)

#en cambio, puedo hacer un print directo y obtener el resultado en pantalla
print(tripler(2))

#o crear una variable cuyo valor sea el return de la función

my_result = tripler(4)

print(my_result)