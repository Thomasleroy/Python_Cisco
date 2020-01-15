from math import pi

def calculate_circle(radius):
    surface = (radius * radius) * pi
    return surface, pi

def animal_age_calculate(human_age):
    '''
    A function that return animal age
    arguments:
    - (int,float) age
    '''
    dog_age = "dog {}".format(round(human_age/7))
    turtle_age ="turtle age {}".format(round(human_age * 1.2))
    return dog_age, turtle_age
