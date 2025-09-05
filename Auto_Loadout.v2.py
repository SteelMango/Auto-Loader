import pydirectinput

# !Problem: If the user adds new stratagems to their arsenal, the positioning to the 
# statagems changes. Need to find a way to adapt

p = pydirectinput

# Click Slot 1
p.press('space') 

# Lazer Dog, Y = 11, X = 0
def Lazer_dog():
    for i in range(1,11):
        p.press('down')
    p.press('space')
Lazer_dog()

# Car, Y = 0 Because it is currently at Y11 from Lazer Dog, x = 1
def car():
    p.press('right')
    p.press('space')
car()

# Mech, Y = 0, X = 1
def mech():
     p.press('right')
     p.press('space')
mech()

def sentry():
    p.press('down')
    p.press('left')
    p.press('space')
sentry()

def recon_passive():
    p.press('right')
    p.press('space')
    p.press('down')
    p.press('space')
recon_passive( )

# Ready Up: All loadouts has been picked 
p.press('b')