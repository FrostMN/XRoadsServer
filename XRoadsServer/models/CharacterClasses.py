from XRoadsServer.models.Ranks import Rank
import math


class CharacterClass(object):

    _name = "Untrained"

    def __str__(self) -> str:
        return self._name

    def get_health_mod(self, rank: Rank):
        """ returns modifier for heath stat """
        return self._health_slow(rank)

    def get_offence_mod(self, rank: Rank):
        """ returns modifier for offence stat """
        return self._offence_normal(rank)

    def get_will_mod(self, rank: Rank):
        """ returns modifier for will stat """
        return self._will_normal(rank)

    def get_dodge_mod(self, rank: Rank):
        """ Returns zero for most clases """
        return rank.value * 0

    def get_hack_mod(self, rank: Rank):
        """ Returns zero for most clases """
        return rank.value * 0

    def _health_fast(self, rank: Rank):
        """ Gets Health modifier for a Fast Health advancement """
        return math.ceil((rank.value - 1) / 2)

    def _health_slow(self, rank: Rank):
        """ Gets Health modifier for a Slow Health advancement """
        return math.ceil((rank.value - 1) / 3)

    def _offence_slow(self, rank: Rank):
        return rank.value * 2

    def _offence_normal(self, rank: Rank):
        return rank.value * 3

    def _offence_fast(self, rank: Rank):
        return rank.value * 7

    def _will_slow(self, rank: Rank):
        if rank.value == 1:
            return 3
        else:
            return 6

    def _will_normal(self, rank: Rank):
        if rank.value == 1:
            return 4
        else:
            return 8

    def _will_fast(self, rank: Rank):
        if rank.value == 1:
            return 5
        else:
            return 10

    def _shinobi_dodge(self, rank: Rank):
        if rank.value == 1:
            return 2
        else:
            return rank.value + 2

    def _shinobi_hack(self, rank: Rank):
        return 5 * rank.value

    def _specialist_hack(self, rank: Rank):
        return (5 * rank.value) + 35


class Assault(CharacterClass):

    _name = "Assault"

    def get_health_mod(self, rank: Rank):
        return super()._health_fast(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_slow(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_fast(rank)

    """ can remove next two over rides """
    def get_dodge_mod(self, rank: Rank):
        return super().get_dodge_mod(rank)

    def get_hack_mod(self, rank: Rank):
        return super().get_hack_mod(rank)


class Grenadier(CharacterClass):

    _name = "Grenadier"

    def get_health_mod(self, rank: Rank):
        return super()._health_fast(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_slow(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_normal(rank)

    """ can remove next two over rides """
    def get_dodge_mod(self, rank: Rank):
        return super().get_dodge_mod(rank)

    def get_hack_mod(self, rank: Rank):
        return super().get_hack_mod(rank)


class Gunner(CharacterClass):

    _name = "Gunner"

    def get_health_mod(self, rank: Rank):
        return super()._health_fast(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_normal(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_normal(rank)

    """ can remove next two over rides """
    def get_dodge_mod(self, rank: Rank):
        return super().get_dodge_mod(rank)

    def get_hack_mod(self, rank: Rank):
        return super().get_hack_mod(rank)


class Ranger(CharacterClass):

    _name = "Ranger"

    def get_health_mod(self, rank: Rank):
        return super()._health_fast(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_normal(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_normal(rank)

    """ can remove next two over rides """
    def get_dodge_mod(self, rank: Rank):
        return super().get_dodge_mod(rank)

    def get_hack_mod(self, rank: Rank):
        return super().get_hack_mod(rank)


class Sharpshooter(CharacterClass):

    _name = "Sharpshooter"

    def get_health_mod(self, rank: Rank):
        return super()._health_slow(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_fast(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_slow(rank)

    """ can remove next two over rides """
    def get_dodge_mod(self, rank: Rank):
        return super().get_dodge_mod(rank)

    def get_hack_mod(self, rank: Rank):
        return super().get_hack_mod(rank)


class Shinobi(CharacterClass):

    _name = "Shinobi"

    def get_health_mod(self, rank: Rank):
        return super()._health_slow(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_slow(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_normal(rank)

    def get_dodge_mod(self, rank: Rank):
        return super()._shinobi_dodge(rank)

    def get_hack_mod(self, rank: Rank):
        return super()._shinobi_hack(rank)


class Specialist(CharacterClass):

    _name = "Specialist"

    def get_health_mod(self, rank: Rank):
        return super()._health_fast(rank)

    def get_offence_mod(self, rank: Rank):
        return super()._offence_slow(rank)

    def get_will_mod(self, rank: Rank):
        return super()._will_fast(rank)

    """ can remove nex override """
    def get_dodge_mod(self, rank: Rank):
        return super().get_dodge_mod(rank)

    def get_hack_mod(self, rank: Rank):
        return super()._specialist_hack(rank)


if __name__ == '__main__':
    # print(health_slow(Rank.Squaddie))

    print(Sharpshooter().get_offence_mod(Rank.Corporal))
