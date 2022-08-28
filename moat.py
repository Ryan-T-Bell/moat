import yfinance as yf

moat = [ "K", "VEEV", "PII", "GILD", "ECL", "BLK", "BA","TYL","MSFT","AMZN","MMM","BIIB",
        "EFX","ETSY","WFC","MAS","EMR","ADBE","ZBH","MELI","GOOGL", "LRCX","WU","CRM",
        "MDT", "GWRE", "NOW", "TER", "META", "INTC", "CPB", "MRK", "STZ", "CSGP", "PM",
        "ROK", "SCHW", "KLAC", "DIS", "ICE", "STT", "BLKB", "HON", "WDAY", "MCHP", "TRU",
        "BRK/B", "TROW", "CMCSA","CMP"
]


def merge_dfs(df0, df1):
        df = df0.merge(df1, on='Date')  
        df['Ratio'] = df['Close_x'] / df['Close_y']
        return calculate_moving_averages(df)

def calculate_moving_averages(df):
        df['50'] = df['Ratio'].rolling(window=50).mean()
        df['200'] = df['Ratio'].rolling(window=200).mean()
        return df

def get_ma_score(df):
        if str(df['50'].tail(1).values >= df['200'].tail(1).values) == '[ True]':
                return 1
        return 0

def get_fundamentals(symbol):
        ticker = yf.Ticker(symbol)
        return [ str(ticker.info['forwardPE']) + ", " + 
                str(ticker.info['priceToBook']) + ", " + 
                str(ticker.info['returnOnEquity']) + ", " + 
                str(ticker.info['debtToEquity']) + ", " + 
                str(ticker.info['grossMargins']) + ", " + 
                str(ticker.info['revenueGrowth'])
        ]

def main():
        print(get_fundamentals('BA'))
 
