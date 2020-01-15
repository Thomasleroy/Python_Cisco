from math import pi

def print_arie(): 
    name="arie"
    print(name)

print_arie()

#2nd function
'''
arguments:

'''
def name_extra(name,name_wife):
    print("hello {}".format(name))
    print("how is your wife {} ?".format(name_wife))

name_extra("thomas","TEST")

"""
comment can be done this way 
"""

def calculate_circle(radius):
    surface = (radius * radius) * pi
    return surface, pi

surface_circle= calculate_circle(5)
print("{}".format(surface_circle))