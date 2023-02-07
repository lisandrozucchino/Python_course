#Pueden existir listas que contengan listas. Y se les puede dar forma.
#Esta tablita tiene cuatro filas y tres columnas, es una "lista en dos dimiensiones"
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#puedo acceder a los elementos a partir de sus "coordenadas" x e y, empezando por arriba a la izquierda. El 1 sería 0;0, mientras que el 9 sería 2;2.
#el orden de las coordenadas es sencillo: el primer[] indica en cuál de las listas está el elemento que busco, y el segundo [] indica la posición dentro de la lista
print(num_grid[0][0])#1
print(num_grid[2][2])#9

