import yfinance as yf
import pandas as pd

watchlist = ['OXY', 'XOM', 'CVX', 'MU', 'TSM', 'NVDA', 'AAPL',
        # MOAT Stocks
        'K', 'VEEV', 'PII', 'GILD', 'ECL', 'BLK', 'BA','TYL','MSFT','AMZN','MMM','BIIB',
        'EFX','ETSY','WFC','MAS','EMR','ADBE','ZBH','MELI','GOOGL', 'LRCX','WU','CRM',
        'MDT', 'GWRE', 'NOW', 'TER', 'META', 'INTC', 'CPB', 'MRK', 'STZ', 'CSGP', 'PM',
        'ROK', 'SCHW', 'KLAC', 'DIS', 'ICE', 'STT', 'BLKB', 'HON', 'WDAY', 'MCHP', 'TRU',
        'TROW', 'CMCSA','CMP'
]

def get_fundamentals(symbol):
        ticker = yf.Ticker(symbol)
        pe = score_forwardPE(ticker)
        pb = score_priceToBook(ticker)
        roe = score_returnOnEquity(ticker)
        roa = score_returnOnAssets(ticker)
        de = score_debtToEquity(ticker)
        return [symbol, pe, pb, roe, roa, de, pe+pb+roe+roa+de]

def score_forwardPE(ticker):
        pe = ticker.info['forwardPE']

        if pe == None or pe < 0 or pe >= 40:
                return 0
        elif pe < 10:
                return 5
        elif pe < 15:
                return 4
        elif pe < 20:
                return 3
        elif pe < 30:
                return 2
        return 1

def score_priceToBook(ticker):
        pb = ticker.info['priceToBook']

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
        roe = ticker.info['returnOnEquity']

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
        roa = ticker.info['returnOnAssets']

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
        de = ticker.info['debtToEquity']

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
        symbols, pe, pb, roe, roa, de, score = [], [], [], [], [], [], []

        for symbol in watchlist:
                print('\n-------------------------')
                print(symbol)
                print('-------------------------')
                ticker = yf.Ticker(symbol)
                symbols.append(symbol)
                pe.append(score_forwardPE(ticker))
                pb.append(score_priceToBook(ticker))
                roe.append(score_returnOnEquity(ticker))
                roa.append(score_returnOnAssets(ticker))
                de.append(score_debtToEquity(ticker))
                score.append(pe[-1] + pb[-1] + roe[-1] + roa[-1] + de[-1])
        
        dict = {
        'Symbol': symbols,
        'Price to Earnings': pe,
        'Price to Book': pb,
        'Return on Equity': roe,
        'Return on Assets': roa,
        'Debt to Equity': de,
        'Score': score
        }

        df = pd.DataFrame(dict)
        print(pd.DataFrame(dict).sort_values(by=['Score']))
        
if __name__ == '__main__':
        main()