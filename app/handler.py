import logging
import sys

from strategy_factory import StrategyFactory
from user import User
from report import Report
from emailer import Emailer

logger = logging.getLogger("Handler")
logger.setLevel(logging.INFO)


def do_calculation(tickers, rpt: Report):

    for ticker in tickers:
        result = StrategyFactory.create(rpt.stg).calculate(ticker, rpt.period, rpt.interval)
        if result is True:
            rpt.add_buy_ticker(ticker)


def run(event, context):
    logger.info('Starting calculations')
    users = User.get_users()

    for a_user in users:
        report_txt = ''

        for a_calculation in a_user.calculations:
            report = Report(a_calculation, a_user)
            do_calculation(a_user.tickers, report)
            report_txt += report.text()
            logger.info(report.text())

        Emailer(logger).send(a_user.email, report_txt)


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    run('', '')