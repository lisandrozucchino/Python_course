num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#para poder recorrer todos los elementos de la lista, debo hacer un nest de loops, es decir, un loop dentro de otro.
#en este caso, el primer loop indicará la FILA en la que trabajaré y el segundo loop devolverá cada elemento.

for row in num_grid:
    for column in row:
        print(column)