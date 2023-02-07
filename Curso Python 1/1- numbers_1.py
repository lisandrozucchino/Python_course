#para trabajar con operaciones matemáticas más avanzadas que las básicas, potencias, redondeos y valores absolutos, tengo que importar "math"
from math import * #es decir, desde "math" traeme todo lo que haya.

#trabajo con números
print(2)

#también puedo hacer operaciones con esos números
print(2 + 2) #4
print(2 * 3) #6
print(8 / 2) #4
print(10 % 3) #1 (calcula el RESTO de dividir el primer número por el segundo)
print(pow(2, 5)) #32 (elevo el primer número a la potencia indicada en el segundo)
print(floor(sqrt(144))) #12. Square root/raíz cuadrada. Incluyo "Floor" para que el resultado no sea 12.0
#por supuesto, también puedo guardar números en variables para usarlos luego.
stamina = 100
golpe = -20
salto = -5
print(stamina) #100
print(stamina + salto + golpe + salto + golpe) #50
#para poder concatenar un número con un string, debo convertirlo en un string antes. Entonces:
stamina_inicial = stamina
stamina_actual = stamina + salto + golpe + salto
print("tu stamina inicial era " + str(stamina_inicial) + ", y tu stamina actual es " +str(stamina_actual))

#También puedo requerir el valor absoluto de un número.
print(abs(golpe))#devolverá 20, no -20.

#Puedo comparar los valores y que me devuelva el que cumpla determinada condición
print(max(golpe, salto)) #aquí devuelve "-5" puesto que es el mayor de los dos.
print(min(salto, stamina)) #y aquí también devolverá "-5" porque es el menor de los dos.

#Para redondear se usa el método "round"
print(round(3.7))
print(round(3.4))

#quitar los decimales con "floor". Es decir, redondea para abajo, sin importar el valor de los decimales.
print(floor(2.95982627344)) #devuelve 2

#para redondear para arriba se usa "ceil"
print(ceil(2.00001)) #devuelve 3