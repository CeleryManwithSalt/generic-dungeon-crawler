# note to self : save points are static
# also this program is gonna need write permission 
# import modules

import time
import random

# items

class chipped_Sword:
    name = "Chipped Sword [C_S]"
    desc = "Your sword, although you can feel a chip in its blade. It probably won't last long."
    hits = 10
    equipped = 0

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
    desc2 = "A ziploc bag of stale and salty cheez-its."
    check = 0

# initialize inventory

inventory = [chipped_Sword.name, unknown_potion1.name, unknown_potion2.name, unknown_potion3.name, useless_map.name, useless_lighter.name, cracker_bag.name]
inventory_range = 7


# switch variables, flags, initialize nomad

use = "N"
tutorial_complete = 0

class Nomad:
    name = ""
    health = 25 # max 50 :^)
    weapon = ""

# functions

# Delay and line space, depending on the situation

def delay(delay, space):
    time.sleep(delay)
    if space == 0:
        space = 0
    else:
        for i in range(space):
            print("")

# displays your current status

def check_self():
    print("Health: " + str(Nomad.health) + "/50")
    print("Equipped Weapon: " + str(Nomad.weapon))

# opens (prints) your inventory
def check_inventory():
    delay(0,1)
    i = 0
    for i in range(inventory_range):
        print(inventory[i])

# inspect the items in your inventory
# this is going to get very long o_o
def inspect_item_F():
    while True:
        delay(0,1)
        inspect_item = str(input("Which item do you wish to inspect? ")).upper()
        delay(0,1)
        if inspect_item == "C_S":
            if chipped_Sword.name in inventory:
                print(chipped_Sword.desc)
                if chipped_Sword.equipped == 0:
                    use = str(input("Equip your chipped sword? (Y/N) ")).upper()
                    if use == "Y":
                        chipped_Sword.equipped = 1
                        Nomad.weapon = chipped_Sword.name
                        use = "N"
                        delay(0,1)
                        print("You equip your sword.")
                    else:
                        delay(0,0) 
            else:
                print("You don't have this sword anymore... ")
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
                if dungeon_save['useless_lighter.check'] == 0:
                    use = str(input("Flick the lighter on? (Y/N) ")).upper()
                    if use == "Y":
                        dungeon_save['useless_lighter.check'] = 1
                        use = "N"
                        delay(0,1)
                        print("You fumble around, but you manage to flick it on.")
                        delay(3,0)
                        print("Nope, you can't see a thing. Looks like you really are blind.")
                        delay(3,0)
                        print("You flick the lighter off.")
                    else:
                        delay(0,0)
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "B_C":
            if cracker_bag.name in inventory:
                if dungeon_save['cracker_bag.check'] == 0:
                    print(cracker_bag.desc)
                    use = str(input("Check the bag? (Y/N) ")).upper()
                    if use == "Y":
                        dungeon_save['cracker_bag.check'] = 1
                        use = "N"
                        delay(0,1)
                        print("You open the bag and stick your hand inside it.")
                        delay(3,0)
                        print("They feel like crackers. You put one in your mouth to make sure.")
                        delay(3,0)
                        print("It tastes like a stale and salty cheez-it. Food is food, though.")
                        delay(3,0)
                        Nomad.health += 5
                        print("You've gained some health back.")

                    else:
                        delay(0,0)
                else:
                    print(cracker_bag.desc2)
            else:
                print("You don't have this anymore... ")
        elif inspect_item == "S":
            check_self()
            delay(0,1)
        elif inspect_item == "C":
            print("You close your bag.")
            delay(0,1)
            break
        else:
            print("You don't have one of those... ")

# saves the Nomad's current status, as well as items interacted with, to a text file.
def save_game():
    dungeon_save['nomad_health'] = Nomad.health
    dungeon_save['chipped_Sword.equipped'] = chipped_Sword.equipped
    dungeon_save['nomad_name'] = Nomad.name
    dungeon_save['tutorial_complete'] = tutorial_complete
    try:
        opensave = open("dungeon_save.txt", "w")
        for x, y in dungeon_save.items():
            save = str(x)
            # print(save)
            opensave.write(str(save))
            save = y
            # print(save)
            opensave.write(" "+ str(save) + "\n")
        opensave.close()
    except:
        print("uhhhh, something went wrong! (bad save?)")

# attempt to load a save, initialize new save otherwise

try:
    dungeon_save = {}
    opensave = open("dungeon_save.txt")

    for line in opensave:
        key, value = line.split()
        try:
            dungeon_save[key] = int((value))
        except:
            dungeon_save[key] = str((value))

    opensave.close()

    if dungeon_save['chipped_Sword.equipped'] == 1:
        Nomad.weapon = chipped_Sword.name
        chipped_Sword.equipped = 1
    Nomad.health = dungeon_save['nomad_health']
    Nomad.name = dungeon_save['nomad_name']
    if dungeon_save['tutorial_complete'] == 1:
        tutorial_complete = 1


except:
    print("No save detected!")
    dungeon_save = {
        'useless_lighter.check': 0 ,
        'cracker_bag.check': 0 ,
    }

# Welcome to the dungeon :)

delay(0,1)
print("A nomad ventures into a vast cavern, searching for loot and adventure.")
delay(4, 0)
print("Whether they make it out is up to you.")
delay(4, 1)
print("Welcome to the dungeon :)")
delay(1, 1)
input("Press enter to continue... ")


# introduction
if tutorial_complete == 0:
    # introduction
    delay(0, 1)
    print("...")
    delay(3,0)
    print("You aren't quite sure when you woke up.")
    delay(3,0)
    print("You can't open your eyes, but it's very dark and damp.")
    delay(3,1)
    print("Oh...")
    delay(1,0)
    print("You can vaguely remember that your eyes were slashed through.")
    delay(4,0)
    print("That's the last thing you remember, at least.")
    delay(3,1)
    print("From somewhere deep within the cave,")
    print("you can hear claws scurrying over rock.")
    delay(5,1)
    print("Awesome.")
    delay(2,1)
    print("You press your fingers against the dog tag around your neck.")
    delay(3,1)
    Nomad.name = str(input("It reads... "))

    # confirm name

    while True: 
        name_confirm = str(input("Does it really read " + Nomad.name + "? (Y/N) ")).upper()
        if name_confirm == "Y":
            break
        else:
            Nomad.name = str(input("What does it read, then? "))

    Nomad.name = Nomad.name.replace(' ', '_')

    # continue intro
    delay(0,1)
    print("You decide to pat yourself down.")
    delay(3,1)
    check_self()
    delay(3,1)
    print("You aren't feeling too great, and your face feels scratched up.")
    delay(3,1)
    print("You decide to feel around and find your bag. You open it.")
    delay(3,1)

    check_inventory()

    delay(3,1)

    inspect_inventory = str(input("Inspect inventory? (Y/N) ")).upper()


    if inspect_inventory == "Y":
        print("Press [C] to cancel at any time.")
        inspect_item_F()
    else:
        delay(0,1)

    print("In the future, you may press [I] to open your inventory,")
    print("and [S] to check yourself.")
    tutorial_complete = 1

delay(3,1)
print("Well, you have nothing better to do now.")
delay(3,0)
print("You figure you might as well get moving.")
delay(3,1)

inspect_inventory = str(input("Placeholder prompt, press [I], [S], or [C] here: ")).upper()

if inspect_inventory == "I":
    check_inventory()
    delay(0,1)
    print("Press [C] to cancel at any time.")
    inspect_item_F()
elif inspect_inventory == "S":
    check_self()
    delay(0,1)
elif inspect_inventory == "C":
    delay(0,1)
else:
    delay(0,1)

print("End of demo :)")
print("Cya later, " + Nomad.name)
delay(0,1)

save_game()