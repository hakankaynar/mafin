import yaml
from yaml.loader import SafeLoader
from calculation import Calculation


class User:

    def __init__(self, uname, email, tickers, calculations: Calculation):
        self.username = uname
        self.email = email
        self.tickers = tickers
        self.calculations = calculations

    @staticmethod
    def get_users_from_file():
        with open('users.yaml') as f:
            cfg = yaml.load(f, Loader=SafeLoader)
            users = []
            for usr in cfg['users']:

                calculations = []
                for calc in cfg['users'][usr]['calculations']:
                    calculations.append(Calculation(strategy=calc['code'], period=calc['period'],
                                                    interval=calc['interval']))

                users.append(User(usr, cfg['users'][usr]['email'],
                                  cfg['users'][usr]["tickers"].split(","), calculations))

            return users
