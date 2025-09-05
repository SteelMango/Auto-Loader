import pyautogui

# Picks the pre-set loadout in Helldivers 2
# 4 Slots, 1 Passive

py = pyautogui


# Select slot 1, then all other slots do not need to be selected. This is because once a stratagem
# is selected, it automatically goes to the next slot

# Select Slot 1
py.moveTo(100,880)
py.click()

# Slots: Dog, Mech, Car, Lazer

def lazer_dog():
    for i in range(0,11):
        py.press('down')
    py.press('space')
lazer_dog()

def car():
    py.press('right')
    py.press('space')
car()

def mech():
    py.press('right')
    py.press('space')
mech()

def lazer():
    for i in range(0,7):
        py.press('up')
    py.press('left')
    py.press('left')
    py.press('space')
lazer()

# Ready up
py.press('b')
 



 
    