from XRoadsServer.models.Character import Character
from typing import Union


class User(object):
    def __init__(self, user_name=None, email=None, confirmed=0, temp_email=None, admin=0, first_name=None,
                 last_name=None, user_id=None, db_user=None):
        if db_user is not None:
            """ If creating user from db call unpack tuple """
            if isinstance(db_user, tuple):
                print(db_user)
                self.user_name = db_user[0]
                self.user_id = db_user[7]
                self.email = db_user[1]
                self.email_confirmed = db_user[2]
                self.temp_email = db_user[3]
                self.admin = db_user[4]
                self.first_name = db_user[5]
                self.last_name = db_user[6]
                self.characters = []
                self.banned = 0
            else:
                raise TypeError
        else:
            """ creating user from parameters """
            self.user_name = user_name
            self.user_id = user_id
            self.email = email
            self.temp_email = temp_email
            self.admin = admin
            self.email_confirmed = confirmed
            self.first_name = first_name
            self.last_name = last_name
            self.characters = []
            self.banned = 0

    def __eq__(self, other):
        """ Override the default Equals behavior """
        return self.user_id == other.user_id \
            and self.email == other.email \
            and self.admin == other.admin \
            and self.email_confirmed == other.email_confirmed \
            and self.first_name == other.first_name \
            and self.last_name == other.last_name

    def is_admin(self):
        print(self.admin)
        if self.admin:
            return True
        else:
            return False

    def is_confirmed(self):
        if self.email_confirmed:
            return True
        else:
            return False

    def is_banned(self):
        if self.banned:
            return True
        else:
            return False

    def add_characters(self, char_list: [Character]):
        self.characters = char_list

    @property
    def id(self):
        return self.user_id

    def set_banned(self, ban: Union[int, bool]):
        if isinstance(ban, int):
            ban = bool(ban)

        self.banned = ban

    def set_verified(self, email_confirmed: Union[int, bool]):
        if isinstance(email_confirmed, int):
            email_confirmed = bool(email_confirmed)

        self.email_confirmed = email_confirmed

    def set_admin(self, admin: Union[int, bool]):
        if isinstance(admin, int):
            admin = bool(admin)

        self.admin = admin
