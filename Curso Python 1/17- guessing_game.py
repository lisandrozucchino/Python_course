#Un while loop puede servir perfectamente para hacer un mini juego de adivinanzas.
#Voy a hacerlo como me parece y después veré cómo lo sugiere el curso.

#una variable para la respuesta y otra para el intento
ans = "Elvis"
att= " "

while att != ans:
    print("What's the name of the cross-eyed cat that lives here?")
    att = input("Your guess here: ")
print("Correct!")

#Eso funciona, ahora intentaré hacer algo un poco más complejo, agregando intentos.

secret_word = "Elvis"
guess = " "
attempts = 3

while guess != secret_word and attempts > 0:
    print("Again, what's the name of that cat?")
    guess = input("Your guess here: ")
    if guess == secret_word:
        print("Yay!")
    else:
        attempts = attempts - 1
        print("Incorrect. You have " + str(attempts) + " attemps left.")