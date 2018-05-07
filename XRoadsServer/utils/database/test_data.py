from XRoadsServer.models.users import User
from XRoadsServer.models.Backgrounds import *
from XRoadsServer.models.Character import Character
from XRoadsServer.models.CharacterClasses import *
from XRoadsServer.models.Weapons import *

users = [
    (User('asouer',  'aaron@asouer.com',    True, None, True,  'Aaron',   'Souer',    1), "test_pw_1"),
    (User('spyndri', 'spyndri@gmail.com',   True, None, False, 'Willson', 'Borchert', 2), "test_pw_2"),
    (User('mlubke',  'MikeLubke@gmail.com', True, None, False, 'Mike',    'Lubke',    3), "test_pw_3"),
]

characters = [
    Character(Resistance(), Assault(), "Aaron Souer", "Drake", AssaultRifle(), None, 1, None, 1),
    Character(Athlete(), Sharpshooter(), "Willson Borchert", "Spin", SniperRifle(), None, 1, None, 2),
    Character(Hunter(), Specialist(), "Mike Lubke", "Darron", SawedOffShotgun(), None, 1, None, 3)
]

