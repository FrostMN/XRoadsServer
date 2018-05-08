from typing import Union
from flask import jsonify as to_json
import json

from XRoadsServer.enums.Ranges import Range
# from XRoadsServer.enums.Ranks import Rank
from XRoadsServer.models.Backgrounds import *
from XRoadsServer.models.CharacterClasses import *
from XRoadsServer.models.Utilities import *
from XRoadsServer.models.Weapons import *


class Character(object):
    """ Character Personal Info"""
    _player_name:     str
    _character_name:  str

    """ Character Stats """
    _rank:        Rank = Rank.Rookie
    _background:  Background
    _class:       CharacterClass

    """ Character Inventory """
    _weapons: [Weapon]
    _utility: [Utility]

    """ Character Ability Scores """
    _aim:       int
    _defence:   int
    _dodge:     int
    _will:      int
    _hacking:   int
    _health:    int
    _mobility:  int

    """ Abilities Chosen """
    _abilities: dict

    def __init__(self, background: Background = None, character_class: CharacterClass= None, player_name: str = None,
                 character_name: str = None, primary_weapon: Weapon = None, utility: Union[list, Utility] = None,
                 level: int=0, abilities: dict=None, player_id: int=0, db=None):
        if db is None:
            """ Initialize Bio """
            self._id = 0
            self._background = background
            self._class = character_class
            self._player_name = player_name
            self._player_id = player_id
            self._character_name = character_name
            self._level_up = level

            """ Initialize Stats """
            self._aim = background.aim
            self._defence = background.defence
            self._dodge = background.dodge
            self._will = background.will
            self._hacking = background.hacking
            self._health = background.health
            self._mobility = background.mobility

            self._abilities = abilities

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
        else:
            # print(db)
            """ Initialize Bio """
            self._id = db[2]
            self._background = db_background(db[5])
            self._player_name = "{first} {last}".format(first=db[0], last=db[1])
            self._character_name = db[4]
            self._level_up = int(db[8])
            self._rank = Rank(db[7])
            self._class = db_class(db[6])

            """ Initialize Stats """
            self._aim = db_background(db[5]).aim
            self._defence = db_background(db[5]).defence
            self._dodge = db_background(db[5]).dodge
            self._will = db_background(db[5]).will
            self._hacking = db_background(db[5]).hacking
            self._health = db_background(db[5]).health
            self._mobility = db_background(db[5]).mobility

            """ Initalize Abilities """
            self._abilities = dict()

            for index in range(len(db)):
                if index > 8:
                    self._abilities.update({Rank(index - 7).name: db[index]})

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

    def __eq__(self, other):
        return self.character_name == other.character_name

    # TODO: these getters need to be finished and maybe corrected
    def get_aim(self, weapon: Weapon=None, range: Union[Range, int]=None):
        if isinstance(range, int):
            range = Range(range)

        if weapon is not None and range is not None:
            if self._rank != Rank.Rookie:
                return self._aim + self._class.get_offence_mod(self._rank) + weapon.get_aim(range)
            else:
                return self._aim
        else:
            if self._class is not None:
                return self._aim + self._class.get_offence_mod(self._rank)
            else:
                return self._aim

    # TODO: needs to be approved
    def get_offense(self):
        if self._rank != Rank.Rookie:
            return self._aim + self._class.get_offence_mod(self._rank)
        else:
            return self._aim

    # TODO: needs to be approved
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

    # TODO: needs to be approved
    def get_will(self):
        if self._rank != Rank.Rookie:
            return self._will + self._class.get_will_mod(self._rank)
        else:
            return self._will

    # TODO: needs to be approved
    def get_hacking(self):
        if self._rank != Rank.Rookie:
            return self._hacking + self._class.get_hack_mod(self._rank)
        else:
            return self._hacking

    # TODO: needs to be approved
    def get_health(self):
        return self._health

    def get_mobility(self):
        encumbrance = 0
        if len(self._utility) > 0:
            encumbrance = len(self._utility)
        return self._mobility - encumbrance

    def set_character_class(self, character_class: CharacterClass):
        self._class = character_class
        self._weapons.append(character_class.sidearm)

    def set_character_name(self, character_name: str):
        print("in set_character_name")
        print(character_name)
        self._character_name = character_name

    @property
    def rank(self):
        return self._rank.name

    @property
    def rank_value(self):
        return self._rank.value

    def set_rank_to(self, rank_to: Union[int, str]):
        if isinstance(rank_to, str):
            rank_to = int(rank_to)
        self._level_up = rank_to

    @property
    def ranks_available(self):
        return self._level_up

    @property
    def can_rank_up(self):
        return self._level_up > 0

    def rank_up(self):
        # print(self._rank)
        # rank_value = int(self._rank.value)
        if self._rank.value < 8:
            self._level_up = self._level_up - 1
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

    @property
    def id(self):
        return self._id

    @property
    def id_str(self):
        return str(self._id)

    @property
    def player_id(self):
        return self._player_id

    @property
    def player_id_str(self):
        return str(self._player_id)

    def add_ability(self, rank: Union[int, Rank], ability):
        if isinstance(rank, int):
            key = Rank(rank)
        else:
            key = rank
        self._abilities.update({key: ability})

    @property
    def abilities(self):
        return self._abilities

    def dump_stats(self, print_stats=False):
        string = "Background: {back}, Rank : {rank}, Class : {ch_class} \n" \
                 "Aim: {aim},\tDefend: {defence},\tDodge: {dodge}\n" \
                 "Will: {will},\tHack: {hack},\tHealth: {health}\n" \
                 "Mobility: {mobile},\tAbilities: {abilities}".format(
                    back=self._background, rank=self._rank.name, aim=self.get_aim(), defence=self.get_defence(),
                    dodge=self.get_dodge(), will=self.get_will(), hack=self.get_hacking(), health=self.get_health(),
                    mobile=self.get_mobility(), ch_class=self.character_class, abilities=self._abilities
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
                       "weapons": weapons, "items": utilities, "stats": stats, "abilities": self._abilities}
        # return to_json(player_dict)
        return player_dict


# helper functions

def db_background(background):
    """ translates stored background string to background object """
    if background == "res":
        return Resistance()
    if background == "sci":
        return Scientist()
    if background == "sca":
        return Scavenger()
    if background == "hun":
        return Hunter()
    if background == "ath":
        return Athlete()


def db_class(character_class):
    if character_class == 'UNT':
        return None
    if character_class == 'ASS':
        return Assault()
    if character_class == 'GRE':
        return Grenadier()
    if character_class == 'GUN':
        return Gunner()
    if character_class == 'RAN':
        return Ranger()
    if character_class == 'SHA':
        return Sharpshooter()
    if character_class == 'SHI':
        return Shinobi()
    if character_class == 'SPE':
        return Specialist()
    if character_class == 'TEC':
        return Technical()
