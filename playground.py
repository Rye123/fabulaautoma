from lib.character import PlayerCharacter, NonPlayerCharacter
from lib.playerclass import *

if __name__ == "__main__":
    lirithid = PlayerCharacter("Lirithid", 10, 6, 10, 6, 10)
    lirithid.classes[CLASS_ENTROPIST] = 6
    lirithid.classes[CLASS_CHIMERIST] = 3
    lirithid.classes[CLASS_WEAPONMASTER] = 1
    print(lirithid)

    fengtian = PlayerCharacter("Feng Tian", 5, 10, 10, 6, 6)
    fengtian.classes[CLASS_SHARPSHOOTER] = 3
    fengtian.classes[CLASS_ROGUE] = 1
    fengtian.classes[CLASS_TINKERER] = 1
    print(fengtian)