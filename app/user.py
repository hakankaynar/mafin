from calculation import Calculation

names = ["AXP", "AMGN", "AAPL", "BA", "CAT", "CSCO", "CVX", "GS", "HD",
         "HON", "IBM", "INTC", "JNJ", "KO", "JPM", "MCD", "MMM", "MRK",
         "MSFT", "NKE", "PG", "TRV", "UNH", "CRM", "VZ", "V", "WBA", "WMT",
         "DIS", "DOW",
         "LMT", "GSK", "KMI", "FMS", "ABBV", "XOM", "VLO", "RIO", "BHP",
         "GOLD", "BTI", "QCOM", "VFC", "O", "FL", "LOW", "TSM",
         "PEP", "NVDA", "EMR", "GLEN.L",

         "ADS.DE", "ALV.DE", "AIR.DE", "BAS.DE", "BAYN.DE", "BMW.DE",
         "CBK.DE", "CON.DE", "DTG.DE", "DB", "DPW.DE", "DTE.DE", "EOAN.DE",
         "HNR1.DE", "HEI.DE", "HEN3.DE", "IFX.DE", "MBG.DE", "MTX.DE", "MUV2.MU",
         "PAH3.DE", "RWE.DE", "SAP", "SIE.DE", "ENR.DE", "VOW3.DE", "VNA.DE", "UPM.HE",
         "IQQA.DE", "EXV6.DE", "IUAE.L", "HDLV.DE",
         "EXV4.DE", "INRA.AS", "NTM.AS",

         "SHEL", "BP", "STLA", "CS.PA", "NESN.SW", "CA.PA", "EQNR.OL"]


class User:

    def __init__(self, uname, email, tickers, calculations: Calculation):
        self.username = uname
        self.email = email
        self.tickers = tickers
        self.calculations = calculations

    @staticmethod
    def get_users():
        calculation = [Calculation("250d", "1d"),
                       Calculation(strategy="SSM"),
                       Calculation(strategy="SME", period="200d")]
        hakan = User("hakan", "hakankaynar@gmail.com", names, calculation)
        gizem = User("gizem", "kocgizem@gmail.com", names, calculation)

        return [hakan, gizem]
