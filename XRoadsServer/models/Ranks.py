from enum import Enum
import itertools


class Rank(Enum):
    Rookie = 0
    Squaddie = 1
    LanceCorporal = 2
    Corporal = 3
    Sergeant = 4
    StaffSergeant = 5
    TechSergeant = 6
    GunnerySergeant = 7
    MasterSergeant = 8


class RankTest(Enum):
    ROOKIE:           dict = {"number": 0, "name": "Rookie"}
    SQUADDIE:         dict = {"number": 1, "name": "Squaddie"}
    LANCE_CORPORAL:   dict = {"number": 2, "name": "Lance Corporal"}
    CORPORAL:         dict = {"number": 3, "name": "Corporal"}
    SERGEANT:         dict = {"number": 4, "name": "Sergeant"}
    STAFF_SERGEANT:   dict = {"number": 5, "name": "Staff Sergeant"}
    TECH_SERGEANT:    dict = {"number": 6, "name": "Tech Sergeant"}
    GUNNERY_SERGEANT: dict = {"number": 7, "name": "Gunnery Sergeant"}
    MASTER_SERGEANT:  dict = {"number": 8, "name": "Master Sergeant"}


_RANKS = {
    0: ['Rookie',           'ROOKIE'],
    1: ['Squaddie',         'SQUADDIE'],
    2: ['Lance Corporal',   'LANCE_CORPORAL'],
    3: ['Corporal',         'CORPORAL'],
    4: ['Sergeant',         'SERGEANT'],
    5: ['Staff Sergeant',   'STAFF_SERGEANT'],
    6: ['Tech Sergeant',    'TECH_SERGEANT'],
    7: ['Gunnery Sergeant', 'GUNNERY_SERGEANT'],
    8: ['Master Sergeant',  'MASTER_SERGEANT'],
}

RankTestTwo = Enum(
    value='RankTestTwo',
    names=itertools.chain.from_iterable(
        itertools.product(v, [k]) for k, v in _RANKS.items()
    )
)

if __name__ == '__main__':
    r = Rank(1)
    print(r.name)
    print(r.value)

    r2 = RankTest.ROOKIE

    print(r2.value["name"])
    print(r2.value["number"])

    r3 = RankTestTwo(5)

    print(r3.name)
    print(r3.value)

    r4 = RankTestTwo.SERGEANT

    print(r4)
