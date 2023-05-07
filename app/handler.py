import logging
import sys
import time

from requests.exceptions import HTTPError
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
            time.sleep(5)
            result = StrategyFactory.create(rpt.stg).calculate(t=ticker, period=rpt.period, interval=rpt.interval)
            if result:
                rpt.add_buy_ticker(TickerData().load(ticker))
        except RuntimeError as e:
            log.warning(e)
        except HTTPError as e:
            log.warning(e)
        except IndexError as e:
            log.warning(e)


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


def run_dl(emailer: Emailer, log):
    log.info('Starting calculations')
    users = User.get_users_dl_from_file()

    for u in users:
        report_txt = ''
        tickers = u.download.download()
        for c in u.calculations:
            report = generate_report(c, tickers, u)
            if report.buy_tickers:
                report_txt += report.text()
                log.info(report.text())

        emailer.send(u.email, report_txt)


def generate_report(c, tickers, u):
    report = Report(c, u)
    for ticker in tickers:
        result = StrategyFactory.create(c.strategy).calculate_downloaded(ticker)
        if result:
            report.add_buy_ticker(TickerData().load(ticker.name))
            time.sleep(5)
    return report


if __name__ == "__main__":
    StrategyConfig.read_cfg()
    run_dl(Emailer(), logger)
