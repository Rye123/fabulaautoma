from lib.core.item import Shield


class ShieldBronzeShield(Shield):
    def __init__(self):
        super().__init__("Bronze Shield", "", 100,
                         False,
                         2, 0, 0)


class ShieldRunicShield(Shield):
    def __init__(self):
        super().__init__("Runic Shield", "", 150,
                         True,
                         2, 2, 0)

