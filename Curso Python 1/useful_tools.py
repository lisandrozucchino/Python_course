#este archivo tiene algunos "módulos", funciones que voy a utilizar en el archivo "modules and pip.py" sin necesidad de escribirlas ahí.

import random

feet_in_mile = 5280

meters_in_kilometers = 1000

metallica = ["Kirk Hamett", "James Hetfield", "Rob Trujillo", "Lars Ulrich"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
