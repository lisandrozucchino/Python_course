#Mad Libs es una especie de juego en el que, a un texto predeterminado, se le agregan palabras elegidas por el usuario. Se piden adjetivos, sustantivos
#o lo que fuera y se completa la historia
#Voy a intentarlo yo solo, fuera del curso. Debajo, voy a copiarlo tal cual está en el video.

#En primera instancia, voy a pedir dos adjetivos y dos sustantivos, que voy a guardar en variables. Después voy a generar un texto en el que 
#se insertarán esas variables.

print("Welcome to my first Mad Libs program! Follow the instructions and enjoy the result!")
adj1 = input("Please, write an adjetive: ")
adj2 = input("Please, write another adjetive: ")
noun1= input("Now, please write a noun: ")
noun2= input("And, finally, a second and last noun: ")

print("Now, let's see how your story goes!")
print("Once upon a time, in a very " + adj1 + " kingdom,\n an incredibly " + adj2 + " princess lived. \n Alongside her, a monstrous " + noun1 + " lurked in the shadows" )
print("Did you like it? Yes, I forgot to use " + noun2 + ", but that happens to the best of us")

#En el video, simplificó e hizo más prints en lugar de \n.

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)