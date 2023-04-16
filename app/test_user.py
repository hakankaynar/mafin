import unittest
from user import User


class TestUser(unittest.TestCase):

    def test_run(self):
        users = User.get_users_from_file()
        self.assertEqual(len(users), 2)
