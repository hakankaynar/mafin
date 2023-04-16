import logging
import sys

from strategy_factory import StrategyFactory
from strategy_config import StrategyConfig
from user import User
from report import Report
from emailer import Emailer
from ticker_data import TickerData

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def do_calculation(tickers, rpt: Report, log):
    for ticker in tickers:
        try:
            result = StrategyFactory.create(rpt.stg).calculate(ticker, rpt.period, rpt.interval)
            if result is True:
                rpt.add_buy_ticker(TickerData().load(ticker))
        except RuntimeError as e:
            log.warn(e)


def run(emailer: Emailer, log):
    log.info('Starting calculations')
    users = User.get_users_from_file()

    for a_user in users:
        report_txt = ''

        for a_calculation in a_user.calculations:
            report = Report(a_calculation, a_user)
            do_calculation(a_user.tickers, report, log)
            if report.buy_tickers:
                report_txt += report.text()
                log.info(report.text())

        emailer.send(a_user.email, report_txt)


if __name__ == "__main__":
    StrategyConfig.read_cfg()
    run(Emailer(), logger)
