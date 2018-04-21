from XRoadsServer.models.CharacterClasses import *
from XRoadsServer.models.Backgrounds import *
from XRoadsServer.models.Ranks import Rank


class Player(object):
    _rank:          Rank = Rank.Rookie
    _background:    Background
    _class:         CharacterClass = None

    """ Player Ability Scores """
    _aim:       int
    _defence:   int
    _dodge:     int
    _will:      int
    _hacking:   int
    _health:    int
    _mobility:  int

    def __init__(self, background: Background):
        self._background = background
        self._aim = background.aim
        self._defence = background.defence
        self._dodge = background.dodge
        self._will = background.will
        self._hacking = background.hacking
        self._health = background.health
        self._mobility = background.mobility

    # TODO: these getters need to be finished and maybe corrected
    def get_aim(self):
        if self._rank != Rank.Rookie:
            return self._aim + self._class.get_offence_mod(self._rank)
        else:
            return self._aim

    def get_offence(self):
        if self._rank != Rank.Rookie:
            return self._aim + self._class.get_offence_mod(self._rank)
        else:
            return self._aim

    def get_defence(self):
        if self._rank != Rank.Rookie:
            return self._defence
        else:
            return self._defence

    # TODO: needs to be implemented
    def get_dodge(self):
        return 1

    def get_will(self):
        return 1

    def get_hacking(self):
        return 1

    def get_health(self):
        return 1

    def get_mobility(self):
        return 1

    def set_character_class(self, char_class: CharacterClass):
        self._class = char_class

    @property
    def rank(self):
        return self._rank.name

    def rank_up(self):
        # print(self._rank)
        if self._rank.value < 8:
            self._rank = Rank(self._rank.value + 1)

    @property
    def character_class(self):
        if self._class is not None:
            return self._class
        else:
            return "Untrained"

    @property
    def background(self):
        return self._background

    def dump_stats(self, print_stats=False):
        string = "Background: {back}, Rank : {rank}, Class : {ch_class} \n" \
                 "Aim: {aim},\tDefend: {defence},\tDodge: {dodge}\n" \
                 "Will: {will},\tHack: {hack},\tHealth: {health}\n" \
                 "Mobility: {mobile}".format(
                    back=self._background, rank=self._rank.name, aim=self.get_aim(), defence=self.get_defence(),
                    dodge=self.get_dodge(), will=self.get_will(), hack=self.get_hacking(), health=self.get_health(),
                    mobile=self.get_mobility(), ch_class=self.character_class
                 )
        if print_stats:
            print(string)
        else:
            return string


"""Actions"""
"""
Move
Fire Weapon
Reload
Overwatch
Hunker Down​
Hack
"""

"""Backgrounds"""
"""
Resistance
Scientist
Scavenger
Hunter
Athlete
"""

"""Classes"""
"""
Assault
Grenadier
Gunner
Ranger
Sharpshooter
Shinobi
Specialist
Technical
"""

"""Enemies"""
"""
ADVENT Trooper
ADVENT Officer
ADVENT Surveillance Drone
Sectoid
"""

if __name__ == '__main__':

    player_one = Player(Athlete())

    # print(player_one.background.name)
    # print(player_one.background.aim)
    # print(player_one.background.defence)
    # print(player_one.background.dodge)
    # print(player_one.background.will)
    # print(player_one.background.hacking)
    # print(player_one.background.health)
    # print(player_one.background.mobility)

    for i in Rank:
        if i == Rank.Rookie:

            player_one.dump_stats(True)
            print("")
            # print("player_one.get_aim():")
            # print("As a {}, {}, {}".format(player_one.rank, player_one.character_class, player_one.background))
            # print("rank number: {}".format(player_one._rank.value))
            # print(player_one.get_aim())
            # print("")

            player_one.rank_up()
            player_one.set_character_class(Assault())
        else:
            # print("player_one.get_aim():")
            # print("As a {}, {}, {}".format(player_one.rank, player_one.character_class, player_one.background))
            # print("rank number: {}".format(player_one._rank.value))
            # print(player_one.get_aim())
            # print("")

            player_one.dump_stats(True)
            print("")
            player_one.rank_up()
pass
