#ahora toca agregar información a los archivos externos.
#comienzo guardando la orden de abrir el archivo en una variable.

external_file = open("24- external.txt", "a") #append significa agregar información al final del archivo.
print(external_file.writable())

#indico que voy a agregar algo al archivo.
external_file.write("Hello, I added this shit from Python")
external_file.write("\nand this shit too! In a new line!")
external_file.write("\nLook at this! Another new line!")

#usar "W" en lugar de "A", es decir write en lugar de append, haría que, al momento de escribir, Python sobreescriba TODO el archivo, no agregaría algo nuevo nada más.

external_file.close()

#pero con write puedo crear un nuevo archivo también.
new_file = open("24- fromPython.txt", "w")

new_file.write("This file was created directly from '24- writing in files.py'")

new_file.close()