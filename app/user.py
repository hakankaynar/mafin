import yaml
from yaml.loader import SafeLoader
from calculation import Calculation
from download import Download


class User:

    def __init__(self, uname, email, calculations: Calculation, download=None, tickers=None):
        self.username = uname
        self.email = email
        self.tickers = tickers
        self.download = download
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

                users.append(User(uname=usr, email=cfg['users'][usr]['email'],
                                  tickers=cfg['users'][usr]["tickers"].split(","),
                                  calculations=calculations))

            return users

    @staticmethod
    def get_users_dl_from_file():
        with open('users_dl.yaml') as f:
            cfg = yaml.load(f, Loader=SafeLoader)
            users = []
            for usr in cfg['users']:
                tickers = cfg['users'][usr]['download']['tickers']
                interval = cfg['users'][usr]['download']['interval']
                period = cfg['users'][usr]['download']['period']

                calculations = []
                for calc in cfg['users'][usr]['calculations']:
                    calculations.append(Calculation(strategy=calc['code'], period=period, interval=interval))

                users.append(User(uname=usr, email=cfg['users'][usr]['email'],
                                  download=Download(tickers, period, interval), calculations=calculations))

            return users
