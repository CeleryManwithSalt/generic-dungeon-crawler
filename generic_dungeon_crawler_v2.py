
# import modules

import time
import random

# items

class chipped_Sword:
    name = "Chipped Sword [C_S]"
    desc = "Your sword, although you can feel a chip in its blade. It probably won't last long."
    hits = 10

class Unknown_Potion:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

unknown_potion1 = Unknown_Potion("Unknown Flask [U_F1]", "A flask. Unfortunately, you can't tell if it's healing, poison, or just hot chocolate.")
unknown_potion2 = Unknown_Potion("Unknown Flask [U_F2]", "A flask. Unfortunately, you can't tell if it's healing, poison, or just hot chocolate.")
unknown_potion3 = Unknown_Potion("Unknown Flask [U_F3]", "A flask. Unfortunately, you can't tell if it's healing, poison, or just hot chocolate.")

class useless_map:
    name = "Map? [M]"
    desc = "A map of the cavern you bought. Unfortunately, you can't read it."

class useless_lighter:
    name = "Lighter [L]"
    desc = "Your lighter, you remember it being black in color."
    check = 0

class cracker_bag:
    name = "Bag of something [B_C]"
    desc = "A ziploc bag, but you don't remember what it contains. Nothing sharp, at least."
    check = 0

# initialize inventory

inventory = [chipped_Sword.name, unknown_potion1.name, unknown_potion2.name, unknown_potion3.name, useless_map.name, useless_lighter.name, cracker_bag.name]
inventory_range = 7


# switch variables, initialize nomad

use = "N"

class Nomad:
    name = ""
    health = 25 # max 50 :^)
    weapon = ""

# functions

# opens (prints) your inventory
def check_inventory():
    print("")
    i = 0
    for i in range(inventory_range):
        print(inventory[i])

# inspect the items in your inventory
# this is going to get very long o_o
def inspect_item_F():
    while True:
        print("")
        inspect_item = str(input("Which item do you wish to inspect? ")).upper()
        print("")
        if inspect_item == "C_S":
            if chipped_Sword.name in inventory:
                print(chipped_Sword.desc)
            else:
                print("You don't have your sword anymore... ")
        elif inspect_item == "U_F1":
            if unknown_potion1.name in inventory:
                print(unknown_potion1.desc)
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "U_F2":
            if unknown_potion2.name in inventory:
                print(unknown_potion2.desc)
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "U_F3":
            if unknown_potion3.name in inventory:
                print(unknown_potion3.desc)
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "M":
            if useless_map.name in inventory:
                print(useless_map.desc)
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "L":
            if useless_lighter.name in inventory:
                print(useless_lighter.desc)
                if useless_lighter.check == 0:
                    use = str(input("Flick the lighter on? (Y/N) ")).upper()
                    if use == "Y":
                        useless_lighter.check = 1
                        dungeon_save.update({"useless_lighter.check": useless_lighter.check})
                        use = "N"
                        print("You fumble around, but you manage to flick it on.")
                        time.sleep(3)
                        print("Nope, you can't see a thing. Looks like you really are blind.")
                        time.sleep(3)
                        print("You flick the lighter off.")
                    else:
                        print("")
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "B_C":
            if cracker_bag.name in inventory:
                print(cracker_bag.desc)
                if cracker_bag.check == 0:
                    use = str(input("Check the bag? (Y/N) ")).upper()
                    if use == "Y":
                        cracker_bag.check = 1
                        dungeon_save.update({"cracker_bag.check": cracker_bag.check})
                        cracker_bag.desc = "A ziploc bag of stale and salty cheez-its."
                        use = "N"
                        print("You open the bag and stick your hand inside it.")
                        time.sleep(3)
                        print("They feel like crackers. You put one in your mouth to make sure.")
                        time.sleep(3)
                        print("It tastes like a stale and salty cheez-it. Food is food, though.")
                    else:
                        print("")
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "C":
            print("You close your bag.")
            print("")
            break
        else:
            print("You don't have one of those... ")

def save_game():
    try:
        opensave = open("dungeon_save.txt", "w")
        for x, y in dungeon_save.items():
            save = str(x)
            print(save)
            opensave.write(str(save))
            save = y
            print(save)
            opensave.write(" "+ str(save) + "\n")
        opensave.close()
    except:
        print("uhhhh, something went wrong! (bad save?)")

# attempt to load a save, initilize new save otherwise


try:
    dungeon_save = {}
    opensave = open("dungeon_save.txt")

    for line in opensave:
        key, value = line.split()
        dungeon_save[key] = int((value))

    print(dungeon_save)

    opensave.close()
except:
    print("No save detected!")
    dungeon_save = {}

useless_lighter.check = dungeon_save['useless_lighter.check']

# Welcome to the dungeon :)

print("")
print("A nomad ventures into a vast cavern, searching for loot and adventure.")
time.sleep(4)
print("Whether they make it out is up to you.")
time.sleep(4)
print("")
print("Welcome to the dungeon :)")
print("")
input("Press enter to continue... ")


# introduction
print("")
print("...")
time.sleep(3)
print("You aren't quite sure when you woke up.")
time.sleep(3)
print("You can't open your eyes, but it's very dark and damp.")
time.sleep(3)
print("Oh...")
time.sleep(1)
print("You can vaguely remember that your eyes were slashed through.")
time.sleep(3) 
print("That's the last thing you remember, at least.")
time.sleep(3)
print("From somewhere deep within the cave,")
print("you can hear claws scurrying over rock.")
time.sleep(5)
print("Awesome.")
time.sleep(2)
print("You press your fingers against the dog tag around your neck.")
time.sleep(3)
Nomad.name = str(input("It reads... "))

# confirm name

while True: 
    name_confirm = str(input("Does it really read " + Nomad.name + "? (Y/N) ")).upper()
    if name_confirm == "Y":
        break
    else:
        Nomad.name = str(input("What does it read, then? "))

# continue intro
print("")
print("You aren't feeling too great, and your face feels pretty scratched up.")
time.sleep(3)
print("You decide to feel around and find your bag. You open it.")
time.sleep(3)

check_inventory()

time.sleep(3)

print("")
inspect_inventory = str(input("Inspect inventory? (Y/N) ")).upper()


if inspect_inventory == "Y":
    print("Press [C] to cancel at any time.")
    inspect_item_F()
else:
    print("")

print("In the future, you may press [I] to open your inventory.")

print("End of demo :)")

#note to self implement health and saving

print(dungeon_save.items())

save_game()