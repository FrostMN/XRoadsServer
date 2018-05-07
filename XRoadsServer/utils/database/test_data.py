from XRoadsServer.models.users import User
from XRoadsServer.models.Backgrounds import *
from XRoadsServer.models.Character import Character
from XRoadsServer.models.CharacterClasses import *
from XRoadsServer.models.Weapons import *

users = [
    (User('asouer',  'asouer@gmail.com',    1, None, 1, 'Aaron',   'Souer'),    "test_pw_1"),
    (User('spyndri', 'spyndri@gmail.com',   1, None, 0, 'Willson', 'Borchert'), "test_pw_2"),
    (User('mlubke',  'MikeLubke@gmail.com', 1, None, 0, 'Mike',    'Lubke'),    "test_pw_3"),
]

characters = [
    Character(Resistance(), Assault(), "Aaron Souer", "Drake", AssaultRifle(), None, 1, None, 1),
    Character(Athlete(), Sharpshooter(), "Willson Borchert", "Spin", SniperRifle(), None, 1, None, 2),
    Character(Hunter(), Specialist(), "Mike Lubke", "Darron", SawedOffShotgun(), None, 1, None, 3)
]

