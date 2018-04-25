from typing import Union
from flask import jsonify as to_json
import json

from XRoadsServer.enums.Ranges import Range
# from XRoadsServer.enums.Ranks import Rank
from XRoadsServer.models.Backgrounds import *
from XRoadsServer.models.CharacterClasses import *
from XRoadsServer.models.Utilities import *
from XRoadsServer.models.Weapons import *


class Player(object):
    """ Player Personal Info"""
    _player_name:     str
    _character_name:  str

    """ Player Stats """
    _rank:        Rank = Rank.Rookie
    _background:  Background
    _class:       CharacterClass = None

    """ Player Inventory """
    _weapons: [Weapon]
    _utility: [Utility]

    """ Player Ability Scores """
    _aim:       int
    _defence:   int
    _dodge:     int
    _will:      int
    _hacking:   int
    _health:    int
    _mobility:  int

    def __init__(self, background: Background, player_name: str = None, character_name: str = None,
                 primary_weapon: Weapon = None, utility: Union[list, Utility] = None):
        """ Initialize Bio """
        self._background = background
        self._player_name = player_name
        self._character_name = character_name

        """ Initialize Stats """
        self._aim = background.aim
        self._defence = background.defence
        self._dodge = background.dodge
        self._will = background.will
        self._hacking = background.hacking
        self._health = background.health
        self._mobility = background.mobility

        """ Initialize Inventory """
        self._weapons = []
        self._utility = []

        """ Load Inventory """
        if primary_weapon is not None:
            self._weapons.append(primary_weapon)

        if utility is not None:
            if isinstance(utility, list):
                for item in utility:
                    self._utility.append(item)
            if isinstance(utility, Utility):
                self._utility.append(utility)

    # TODO: these getters need to be finished and maybe corrected
    def get_aim(self, weapon: Weapon, range: Union[Range, int]):
        if isinstance(range, int):
            range = Range(range)

        if self._rank != Rank.Rookie:
            return self._aim + self._class.get_offence_mod(self._rank) + weapon.get_aim(range)
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

    # TODO: needs to be approved
    def get_dodge(self):
        if self._rank != Rank.Rookie:
            return self._dodge + self._class.get_dodge_mod(self._rank)
        else:
            return self._dodge

    # TODO: needs to be implemented
    def get_will(self):
        return 1

    # TODO: needs to be implemented
    def get_hacking(self):
        return 1

    # TODO: needs to be implemented
    def get_health(self):
        return 1

    def get_mobility(self):
        encumbrance = 0
        if len(self._utility) > 0:
            encumbrance = len(self._utility)
        return self._mobility - encumbrance

    def set_character_class(self, character_class: CharacterClass):
        self._class = character_class
        self._weapons.append(character_class.sidearm)

    @property
    def rank(self):
        return self._rank.name

    def rank_up(self):
        # print(self._rank)
        # rank_value = int(self._rank.value)
        if self._rank.value < 8:
            self._rank = Rank(self._rank.value + 1)

    @property
    def character_class(self):
        if self._class is not None:
            return self._class
        else:
            return "Untrained"

    @property
    def player_name(self):
        return self._player_name

    @property
    def character_name(self):
        return self._character_name

    @property
    def background(self):
        return self._background

    @property
    def weapons(self):
        return self._weapons

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

    def to_dict(self):

        weapons = []
        utilities = []

        for weapon in self._weapons:
            weapons.append(weapon.to_dict())

        for item in self._utility:
            utilities.append(item.to_dict())

        stats = {"aim": self._aim, "defence": self._defence, "dodge": self._dodge, "will": self._will,
                 "hacking": self._hacking, "health": self._health, "mobility": self._mobility}

        if self._class:
            character_class = self._class.name
        else:
            character_class = "Untrained"

        player_dict = {"player_name": self.player_name, "character_name": self._character_name,
                       "rank": self._rank.value, "background": self._background.name, "class": character_class,
                       "weapons": weapons, "items": utilities, "stats": stats}
        # return to_json(player_dict)
        return player_dict


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

    for i in Rank:
        if i == Rank.Rookie:

            player_one.dump_stats(True)
            print("")

            player_one.rank_up()
            player_one.set_character_class(Assault())
        else:

            player_one.dump_stats(True)
            print("")
            player_one.rank_up()
pass
