from lib.character import PlayerCharacter, NonPlayerCharacter
from lib.playerclass import *

if __name__ == "__main__":
    lirithid = PlayerCharacter("Lirithid", 10, 6, 10, 6, 10)
    lirithid.player_classes += [ClassEntropist(6), ClassChimerist(3), ClassWeaponmaster(1)]
    lirithid.compute()
    print(lirithid)

    fengtian = PlayerCharacter("Feng Tian", 5, 10, 10, 6, 6)
    fengtian.player_classes += [ClassSharpshooter(3), ClassRogue(1), ClassTinkerer(1)]
    fengtian.compute()
    print(fengtian)

