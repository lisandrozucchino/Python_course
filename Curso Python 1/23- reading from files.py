#Python puede leer y escribir en archivos con otras extensiones (TXT, CSV, etc)
#Para este ejemplo, creé el archivo "external.txt", que contiene solamente texto.

#el primer paso es ABRIR ese archivo. Como ambos están en el mismo directorio, alcanza con escribir el nombre del archivo. Debería indicar el path si se encontrara en otra carpeta. Hay distintos "modos" en los que se abre el archivo. "r" significa "read", "w" significa "write", "a" significa "append" y el último sería "r+", que permite leer y escribir.
#Guardo todo en una variable.
external_file = open("23- external.txt", "r")

#me aseguro que el archivo pueda ser leído por Python. Si devuelve "true", puedo proseguir.
print(external_file.readable())

#ahora entonces trato de traer toda la información.
#print(external_file.read())

print(external_file.writable())
#se trata de un archivo de texto, Python puede identificar cada renglón. Con "Readline", si los pongo consecutivamente, puedo ir accediendo a los renglones.
#print(external_file.readline())
#print(external_file.readline())
#print(external_file.readline())

#Puedo guardar todos los renglones separados en un array.
#print(external_file.readlines())

all_Stars = external_file.readlines()

#print(all_Stars[1])

#puedo hacer un loop utilizando el archivo.
#for player in external_file.readlines():
#    print(player)

for player in all_Stars:
    print(player)

#Al terminar de usar el archivo, siempre hay que cerrarlo.
external_file.close()

print(all_Stars[1])
