"""
This code is for equipment. Still not entirely sure about the implementation, much of this is a WIP for now.
"""


class Item:
    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc


class Weapon(Item):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)


class Armor(Item):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)


class Shield(Item):
    def __init__(self, name: str, desc: str):
        super().__init__(name, desc)
