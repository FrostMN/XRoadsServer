from XRoadsServer.application import app
import XRoadsServer.utils.database.test_connection as database
import XRoadsServer.utils.database.users as users
from XRoadsServer.models.users import User
from XRoadsServer.utils.database.test_data import users as test_users, characters as test_chars
from config import TestingConfig
import unittest


class TestUsers(unittest.TestCase):

    users.db.config.MYSQL_CONN = TestingConfig.MYSQL_CONN

    def setUp(self):
        database.init_db()
        database.load_db()

    def test_validate_admin_one_good_password_main_db(self):

        self.assertTrue(users.valid_password("asouer", "123"))
        self.assertFalse(users.valid_password("asouer", "321"))

    def test_validate_admin_one_good_password(self):

        self.assertTrue(users.valid_password("asouer", "test_pw_1"))
        self.assertFalse(users.valid_password("asouer", "test_pw_b"))

    def test_get_correct_user(self):

        db_user = users.get_user_by_id(1)
        t_user = test_users[0][0]

        self.assertEqual(db_user, t_user)


class TestCharacters(unittest.TestCase):

    users.db.config.MYSQL_CONN = TestingConfig.MYSQL_CONN

    def setUp(self):
        database.init_db()
        database.load_db()

    def test_validate_get_correct_char_from_db(self):
        db_char = users.get_character_by_id(1)
        t_char = test_chars[0]

        self.assertEqual(db_char, t_char)

    def test_character_aim_score(self):

        expected_attack = 75

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        self.assertEqual(expected_attack, db_user.characters[0].get_aim())

    def test_character_defence_score(self):

        expected_defence = 0

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        self.assertEqual(expected_defence, db_user.characters[0].get_defence())

    def test_character_dodge_score(self):

        expected_dodge = 12

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        self.assertEqual(expected_dodge, db_user.characters[0].get_dodge())

    def test_character_will_score(self):

        expected_will = 103

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        self.assertEqual(expected_will, db_user.characters[0].get_will())

    def test_character_hacking_score(self):

        expected_hacking = 30

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        print(db_user.characters[0].get_hacking())

        self.assertEqual(expected_hacking, db_user.characters[0].get_hacking())

    def test_character_health_score(self):

        expected_health = 4

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        print(db_user.characters[0].get_health())

        self.assertEqual(expected_health, db_user.characters[0].get_health())

    def test_character_mobility_score(self):

        expected_mobility = 5

        db_user = users.get_user_by_id(1)
        db_char = users.get_character_by_id(1)
        db_user.add_characters([db_char])

        print(db_user.characters[0].get_mobility())

        self.assertEqual(expected_mobility, db_user.characters[0].get_mobility())


if __name__ == '__main__':
    unittest.main()
