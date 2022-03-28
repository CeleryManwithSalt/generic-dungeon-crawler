
# import modules

import time
import random

# Welcome to the dungeon :)

print("A nomad ventures into a vast cavern, searching for loot and adventure.")
time.sleep(4)
print("Whether they make it out is up to you.")
time.sleep(4)
print("")
print("Welcome to the dungeon :)")
print("")
input("Press any key to continue. ")

# items

class chipped_Sword:
    name = "Chipped Sword"
    desc = "Your sword, although you can feel a chip in its blade. It probably won't last long."
    hits = 10

unknown_potion1 = "Unknown Flask"
unknown_potion2 = "Unknown Flask"
unknown_potion3 = "Unknown Flask"
unknown_potion_desc = "A flask. Unfortunately, you can't tell if it's healing, poison, or just water."

useless_map = "Map?"
useless_map_desc = "A map of the cavern you bought. Unfortunately, you can't read it."

useless_lighter = "Lighter"
useless_lighter_desc = "Your lighter, you remember it being black in color."

cracker_bag = "Bag of something"
cracker_bag_desc = "A ziploc bag, but you don't remember what it contains."

# initialize inventory

inventory = [chipped_Sword.name, unknown_potion1, unknown_potion2, unknown_potion3, useless_map, useless_lighter, cracker_bag]
inventory_range = 7

# functions

def check_inventory():
    print("")
    i = 0
    for i in range(inventory_range):
        print(inventory[i])

def inspect_item_F():
    inspect_item = input("Pick, 1-" + str(inventory_range) + " ")
    while True:
        if type(inspect_item) == str:
            try:
                inspect_item = int(inspect_item)
                if inspect_item > inventory_range:
                    inspect_item = input("Out of range! Try again. ")
            except ValueError:
                inspect_item = inspect_item.upper()
                if inspect_item == "C":
                    print("okay")
                    break
                else:
                    inspect_item = input("Invalid input! Try again. ")
        else:
            if inspect_item == 1:
                print(chipped_Sword.desc)
                break
            

inspect_item_F()

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
time.sleep(1)
print("That's the last thing you remember, at least.")
time.sleep(3)
print("From somewhere deep within the cave,")
print("you can hear claws scurrying over rock.")
time.sleep(3)
print("Awesome.")
time.sleep(2)
print("You press your fingers against the dog tag around your neck.")
time.sleep(3)
name = str(input("It reads... "))

# confirm name

while True: 
    name_confirm = str(input("Does it really read " + name + "? (Y/N) ")).upper()
    if name_confirm == "Y":
        break
    else:
        name = str(input("What does it read, then? "))

# continue intro

print("You decide to feel around and find your bag. You open it.")
time.sleep(3)

check_inventory()

time.sleep(3)
inspect_inventory = str(input("Inspect inventory? (Y/N)")).upper()


if inspect_inventory == "Y":
    print("Press [C] to cancel at any time.")
    inspect_item_F()
else:
    print("In the future, you may press [I] to open your inventory, and [I] again to inspect.")
