import yfinance as yf
import pandas as pd

watchlist = [
        # My List
        'MU','TSM','NVDA','AAPL','MATX','TENB','CRWD','TEAM','EGY',

        # Oil
        'OXY', 'XOM', 'CVX',

        # Uranium / Nuclear Power
        'UEC',

        # Cybersecurity
        'BAH','CRWD','PANW','CTXS','ZS','JNPR','CHKP','VMW','CACI','AKAM',
        'FTNT','CYBR','MNDT','QLYS','SAIC','OKTA','DOCU','S','TENB',
        'BB','CALX','ALRM','RPD','VRNS','MANT','PING','MCRO','NETC','DARK',
        'TMV','EVBG','KNBE','YOU','ADTN','RDWR','ATEN','MYEG','ABST',
        'KAPE','TLS','CGNT','OSPN','YSN','SPLK','DDOG','NET',

        # DATORAMA
        'GEO','CACC','IAC','RFP','ALLY','WFC',

        # MOAT Stocks
        'K', 'VEEV', 'PII', 'GILD', 'ECL', 'BLK', 'BA','TYL','MSFT','AMZN','MMM','BIIB',
        'EFX','ETSY','WFC','MAS','EMR','ADBE','ZBH','MELI','GOOGL', 'LRCX','WU','CRM',
        'MDT', 'GWRE', 'NOW', 'TER', 'META', 'INTC', 'CPB', 'MRK', 'STZ', 'CSGP', 'PM',
        'ROK', 'SCHW', 'KLAC', 'DIS', 'ICE', 'STT', 'BLKB', 'HON', 'WDAY', 'MCHP', 'TRU',
        'TROW', 'CMCSA','CMP'
]

commodities = [
        # Oil
        'OXY', 'XOM', 'CVX',

        # Uranium / Nuclear Power
        'UEC'
]

cyber_security = [
        'BAH','CRWD','PANW','CTXS','ZS','JNPR','CHKP','VMW','CACI','AKAM',
        'FTNT','CYBR','MNDT','QLYS','SAIC','OKTA','DOCU','S','TENB',
        'BB','CALX','ALRM','RPD','VRNS','MANT','PING','MCRO','NETC','DARK',
        'TMV','EVBG','KNBE','YOU','ADTN','RDWR','ATEN','MYEG','ABST',
        'KAPE','TLS','CGNT','OSPN','YSN','SPLK','DDOG','NET'
]

moat = [
        'K', 'VEEV', 'PII', 'GILD', 'ECL', 'BLK', 'BA','TYL','MSFT','AMZN','MMM','BIIB',
        'EFX','ETSY','WFC','MAS','EMR','ADBE','ZBH','MELI','GOOGL', 'LRCX','WU','CRM',
        'MDT', 'GWRE', 'NOW', 'TER', 'META', 'INTC', 'CPB', 'MRK', 'STZ', 'CSGP', 'PM',
        'ROK', 'SCHW', 'KLAC', 'DIS', 'ICE', 'STT', 'BLKB', 'HON', 'WDAY', 'MCHP', 'TRU',
        'TROW', 'CMCSA','CMP'      
]

def get_fundamentals(symbol):
        ticker = yf.Ticker(symbol)
        peg = score_peg(ticker)
        pb = score_priceToBook(ticker)
        roe = score_returnOnEquity(ticker)
        roa = score_returnOnAssets(ticker)
        de = score_debtToEquity(ticker)
        return [symbol, peg, pb, roe, roa, de, peg+pb+roe+roa+de]

def score_peg(ticker):
        try:
                peg = ticker.info['pegRatio']
        except:
                return 0

        if peg == None or peg < 0 or peg >= 4:
                return 0
        elif peg < 1:
                return 5
        elif peg < 1.5:
                return 4
        elif peg < 2:
                return 3
        elif peg < 4:
                return 2
        return 1

def score_priceToBook(ticker):
        try:
                pb = ticker.info['priceToBook']
        except:
                return 0

        if pb == None or pb < 0 or pb >= 10:
                return 0
        elif pb < 1:
                return 5
        elif pb < 2:
                return 4
        elif pb < 4:
                return 3
        elif pb < 8:
                return 2
        return 1

def score_returnOnEquity(ticker):
        try:
                roe = ticker.info['returnOnEquity']
        except:
                return 0

        if roe == None or roe < 0:
                return 0
        elif roe > 0.4:
                return 5
        elif roe > 0.3:
                return 4
        elif roe > 0.2:
                return 3
        elif roe > 0.1:
                return 2
        return 1

def score_returnOnAssets(ticker):
        try:
                roa = ticker.info['returnOnAssets']
        except:
                return 0

        if roa == None or roa < 0:
                return 0
        elif roa > 0.4:
                return 5
        elif roa > 0.3:
                return 4
        elif roa > 0.2:
                return 3
        elif roa > 0.1:
                return 2
        return 1

def score_debtToEquity(ticker):
        try:
                de = ticker.info['debtToEquity']
        except:
                return 0

        if de == None or de < 0 or de >= 30:
                return 0
        elif de < 1:
                return 5
        elif de < 2:
                return 4
        elif de < 4:
                return 3
        elif de < 10:
                return 2
        return 1

def main():
        symbols, peg, pb, roe, roa, de, score = [], [], [], [], [], [], []

        for symbol in watchlist:
                print(symbol)
                ticker = yf.Ticker(symbol)
                symbols.append(symbol)
                peg.append(score_peg(ticker))
                pb.append(score_priceToBook(ticker))
                roe.append(score_returnOnEquity(ticker))
                roa.append(score_returnOnAssets(ticker))
                de.append(score_debtToEquity(ticker))
                score.append(peg[-1] + pb[-1] + roe[-1] + roa[-1] + de[-1])
        
        dict = {
        'Symbol': symbols,
        'Price to Earnings': peg,
        'Price to Book': pb,
        'Return on Equity': roe,
        'Return on Assets': roa,
        'Debt to Equity': de,
        'Score': score
        }

        df = pd.DataFrame(dict).sort_values(by=['Score'])
        df.to_csv('results.csv', index = False)
        
if __name__ == '__main__':
        main()