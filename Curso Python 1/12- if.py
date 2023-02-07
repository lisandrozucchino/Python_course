#En un "if", se le indica al programa qué debe hacer en el caso que se cumpla o no alguna condición.

#comienzo con una variable que contiene un booleano que, cuando el programa la lea, interpretará que se ha cumplido o no determinada condición.
is_male = False
is_tall = False
is_strong = True
is_green = False
is_Ironman = True
is_alive = False

if is_male:
    print("The character is male")
else:
    print("The character is not male, do not assume is a female, you nazi bastard")

#ok, cuando hay más de una condición que queremos considerar, tiene que haber un conector lógico entre los valores de las variables.
#el primero es "or", en el que el "if" se ejecutará si una de las dos condiciones se cumple. 

if is_male or is_strong: #en este ejemplo, si "is_male" es true, pero "is_strong" es falso, el programa considera que se cumple el if.
    print("This guy shouldn't compete against women")
else:
    print("Again, no male and not tall, but you can't assume we are talking about a short female")

#otro conector lógico es "and" e indica que el if sólo se ejecutará en el caso de cumplirse AMBAS condiciones.
#else if se escribe "elif"
if is_strong and is_green:
    print("Hey, it's the Hulk")
#para indicar que se tiene que cumplir un FALSE, se indica un "not"
elif is_strong and is_Ironman and not(is_alive):
    print("He's not the Hulk, he's Ironman!")
else:
    print("We are not talking about an Avenger, just a regular strong guy")

