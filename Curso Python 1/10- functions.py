#las funciones son una sucesión de instrucciones.
#utilizan la palabra clave "def"
#el código de la función DEBE estar indentado. Python no reconoce el código si no respeta la indentación.

#las funciones pueden (o no) tener parámetros. En caso de no tener un parámetro, se ejecutará al llamarla y hará siempre lo mismo.

#defino la función sin parámetro
def normal_salute():
    print("Yeah, this is always the same")

#llamo a la función sin parámetro.
normal_salute()

#defino la función con parámetro.
def say_hi(name):
    print("Well... Hello there, " + name)

#creo una variable para utilizar como parámetro.
nombre_usuario = input("Please, tell me your name: ")

#llamo a la función con parámetro.
say_hi(nombre_usuario)

#puedo utilizar funciones previamente definidas dentro de nuevas funciones.
def combo(a, b):
    say_hi(a)
    result = float(b) * 2
    resultado = str(round(result))
    print("El doble de tu número elegido es " + resultado)

#defino los parámetros vía input
param1 = input("Por favor, dame otro nombre para trabajar: ")
param2 = input("Y ahora, necesito que elijas un número: ")

#llamo a la función "combo con los parámetros que obtuve"
combo(param1, param2)

