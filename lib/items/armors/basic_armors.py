from lib.core.item import Armor


class Armor_NoArmor(Armor):
    def __init__(self):
        super().__init__("No Armor", "", 0,
                         False,
                         "DEX", "INS", 0)


class Armor_SilkShirt(Armor):
    def __init__(self):
        super().__init__("Silk Shirt", "", 100,
                         False,
                         "DEX", "INS+2", -1)


class Armor_TravelGarb(Armor):
    def __init__(self):
        super().__init__("Travel Garb", "", 100,
                         False,
                         "DEX+1", "INS+1", -1)


class Armor_CombatTunic(Armor):
    def __init__(self):
        super().__init__("Combat Tunic", "", 150,
                         False,
                         "DEX+1", "INS+1", 0)


class Armor_SageRobe(Armor):
    def __init__(self):
        super().__init__("Sage Robe", "", 200,
                         False,
                         "DEX+1", "INS+2", -2)


class Armor_Brigandine(Armor):
    def __init__(self):
        super().__init__("Brigandine", "", 150,
                         True,
                         "10", "INS", -2)


class Armor_BronzePlate(Armor):
    def __init__(self):
        super().__init__("Bronze Plate", "", 200,
                         True,
                         "11", "INS", -3)


class Armor_RunicPlate(Armor):
    def __init__(self):
        super().__init__("Runic Plate", "", 250,
                         True,
                         "11", "INS+1", -3)


class Armor_SteelPlate(Armor):
    def __init__(self):
        super().__init__("Steel Plate", "", 300,
                         True,
                         "12", "INS", -4)

