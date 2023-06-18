import unittest
from user import User


class TestDownload(unittest.TestCase):

    def test_run(self):
        users = User.get_users_dl_from_file()
        for u in users:
            r = u.download.download()
            print(r)
