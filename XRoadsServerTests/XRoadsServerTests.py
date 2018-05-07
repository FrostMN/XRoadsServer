from XRoadsServer.application import app
import XRoadsServer.utils.database.test_connection as database
import XRoadsServer.utils.database.users as users
import unittest


class TestUsers(unittest.TestCase):

    def setUp(self):
        database.init_db()
        database.load_db()

    def test_validate_admin_one_good_password_main_db(self):
        self.assertTrue(users.valid_password("asouer", "123"))
        self.assertFalse(users.valid_password("asouer", "321"))

    def test_validate_admin_one_good_password(self):
        self.assertTrue(users.valid_password("asouer", "test_pw_1"))
        self.assertFalse(users.valid_password("asouer", "test_pw_b"))


if __name__ == '__main__':
    unittest.main()
