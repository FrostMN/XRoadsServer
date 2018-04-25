from XRoadsServer.enums.Ranges import Range
import math, json


class Weapon(object):

    _name:        str
    _damage:      int
    _critical:    int
    _lethality:   int
    _clip:        int
    _point_blank: int
    _short:       int
    _medium:      int
    _long:        int

    @property
    def name(self):
        return self._name

    @property
    def lethality(self):
        return self._lethality

    def get_aim(self, range: Range):
        if range == Range.POINT_BLANK:
            return self._point_blank
        if range == Range.SHORT:
            return self._short
        if range == Range.MEDIUM:
            return self._medium
        if range == Range.LONG:
            return self._long

    def get_damage(self):
        return self._damage

    def get_critical(self):
        return self._damage + self._critical

    def get_graze(self):
        return math.floor(self._damage / 2)

    def __str__(self) -> str:
        return self._name

    def to_dict(self):

        weapon_dict = {"name": self._name, "damage": self._damage, "critical": self._critical,
                       "lethality": self._lethality, "clip": self._clip, "point_blank": self._point_blank,
                       "short": self._short, "medium": self._medium, "long": self._long}
        return weapon_dict


class AssaultRifle(Weapon):

    _name: str = "Assault Rifle"
    _damage = 4
    _critical = 2
    _lethality = 0
    _clip = 4
    _point_blank = 30
    _short = 15
    _medium = 0
    _long = -15


class Cannon(Weapon):

    _name = "Cannon"
    _damage = 5
    _critical = 2
    _lethality = 0
    _clip = 3
    _point_blank = -10
    _short = 0
    _medium = 0
    _long = 0


class SubmachineGun(Weapon):

    _name = "Submachine Gun (SMG)"
    _damage = 3
    _critical = 1
    _lethality = 0
    _clip = 2
    _point_blank = 30
    _short = 10
    _medium = -15
    _long = -75


class Shotgun(Weapon):

    _name = "Shotgun"
    _damage = 5
    _critical = 2
    _lethality = 15
    _clip = 4
    _point_blank = 60
    _short = 10
    _medium = -55
    _long = -100


class SniperRifle(Weapon):

    _name = "Sniper Rifle"
    _damage = 5
    _critical = 2
    _lethality = 10
    _clip = 3
    _point_blank = -30
    _short = -15
    _medium = 0
    _long = 0


class Sidearm(Weapon):

    _aim: int

    @property
    def aim(self):
        return self._aim


class ArcThrower(Sidearm):

    _name = "Arc Thrower"
    _aim = 5
    _damage = 0
    _critical = 0
    _lethality = 0
    _clip = 0
    _point_blank = 30
    _short = 15
    _medium = 0
    _long = -15


class CombatKnife(Sidearm):

    _name = "Combat Knife"
    _aim = 20
    _damage = 3
    _critical = 3
    _lethality = 20
    _clip = 0
    _point_blank = 0
    _short = -1000
    _medium = -1000
    _long = -1000


class Gauntlet(Sidearm):

    _name = "Gauntlet"


class Gremlin(Sidearm):

    _name = "Gremlin"


class GrenadeLauncher(Sidearm):

    _name = "Grenade Launcher"


class Holotargeter(Sidearm):

    _name = "Holotargeter"


class SawedOffShotgun(Sidearm):

    _name = "Sawed-Off Shotgun"
    _aim = 5
    _damage = 7
    _critical = 2
    _lethality = 15
    _clip = 2
    _point_blank = 60
    _short = -35
    _medium = -100
    _long = -100


class Sword(Sidearm):

    _name = "Sword"
    _aim = 20
    _damage = 4
    _critical = 2
    _lethality = 10
    _clip = 0
    _point_blank = 0
    _short = -1000
    _medium = -1000
    _long = -1000
