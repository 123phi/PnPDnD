import random

class Item(object):

    def __init__(self, name, lvl, desc, cost, rarity):
        self.name = name
        self.level = lvl
        self.description = desc
        self.cost = cost
        self.rarity = rarity

    def __str__(self):
        string = "Item: " + str(self.name) + " "
        string += "Level: " + str(self.level) + " "
        string += "Description: " + str(self.description) + " "
        string += "Cost: " + str(self.cost) + " "
        string += "Rarity: " + str(self.rarity)
        return string

shop_types = ["Magic", "Armor", "Weapons", "Misc"]
magic_item_list = [Item("Ring of power", 1, "+1 strength, invisibility", "1000000", "4"),
                   Item("Sword of Death", 1, "+3 strength, +1 dead body", "10000", "3")]
#armor_item_list
#weapon_item_list
#misc_item_list

def num_shop_gen():
    """ Generates 4 numbers representing the number of shops in a given town. """
    nums = [random.randint(0, 2) for _ in range(4)]
    return nums



def choose_magic_item():
    print random.choice(magic_item_list)

choose_magic_item()
