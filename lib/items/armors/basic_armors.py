from lib.core.item import Armor


class ArmorNoArmor(Armor):
    def __init__(self):
        super().__init__("No Armor", "", 0,
                         False,
                         "DEX", "INS", 0)


class ArmorSilkShirt(Armor):
    def __init__(self):
        super().__init__("Silk Shirt", "", 100,
                         False,
                         "DEX", "INS+2", -1)


class ArmorTravelGarb(Armor):
    def __init__(self):
        super().__init__("Travel Garb", "", 100,
                         False,
                         "DEX+1", "INS+1", -1)


class ArmorCombatTunic(Armor):
    def __init__(self):
        super().__init__("Combat Tunic", "", 150,
                         False,
                         "DEX+1", "INS+1", 0)


class ArmorSageRobe(Armor):
    def __init__(self):
        super().__init__("Sage Robe", "", 200,
                         False,
                         "DEX+1", "INS+2", -2)


class ArmorBrigandine(Armor):
    def __init__(self):
        super().__init__("Brigandine", "", 150,
                         True,
                         "10", "INS", -2)


class ArmorBronzePlate(Armor):
    def __init__(self):
        super().__init__("Bronze Plate", "", 200,
                         True,
                         "11", "INS", -3)


class ArmorRunicPlate(Armor):
    def __init__(self):
        super().__init__("Runic Plate", "", 250,
                         True,
                         "11", "INS+1", -3)


class ArmorSteelPlate(Armor):
    def __init__(self):
        super().__init__("Steel Plate", "", 300,
                         True,
                         "12", "INS", -4)

