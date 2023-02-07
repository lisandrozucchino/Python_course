#este es un experimento de "traducción", para cambiar letras de la frase o palabra que recibimos y devolverla cambiada... Casi un encriptador.

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter == "a" or letter == "o":
            translation = translation + "puto"
        else:
            translation = translation + letter
    return translation

print(translator("comida para llevar"))


#la manera correcta de hacerlo es:

def translator2(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "puto"
        else:
            translation = translation + letter
    return translation

print(translator2("comida para llevar"))