import random
from re import X
elements = ["Actinium","Silver","Aluminum"]

X = random.choice(elements)
#print( X)

print("H-Mg-Ti-O-Au-Ni-Pt-Er-W-Xe-Zn-Li")
print("Pd                            Na")
print("Cu   Chemical Elements Quiz   Fe")
print("Sc                            Te")
print("H-Mg-Ti-O-Au-Ni-Pt-Er-W-Xe-Zn-Li")

guess = None

while guess != X:
    guess = str(input("teka: "))
    guess = str (guess)


    if X == guess:
        print("You genius!")
    else:
        print("Sorry, try again")